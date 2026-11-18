from pathlib import Path
import tempfile
import unittest

from scraper import ROOT, classify, load_config, parse_trending, read_json, trending_url, update_archive


CARD = '''<html><a href="/login">Sign in</a><article class="Box-row">
<h2><a href="/demo/llm-kit"><svg><path /></svg>demo / llm-kit</a></h2>
<p>A &amp; B <b>LLM</b> toolkit. 中文简介</p>
<span itemprop="programmingLanguage">Python</span>
<a href="/demo/llm-kit/stargazers"><svg></svg>12,345</a>
<a href="/demo/llm-kit/forks">67</a><span>123 stars today</span>
</article></html>'''


class ScraperTests(unittest.TestCase):
    def setUp(self):
        self.config = load_config(ROOT / 'config.json')

    def repo(self, name='demo/llm-kit'):
        repo = parse_trending(CARD)[0]
        repo.update(name=name, categories=['LLMs & Generative AI'], sources=[{'language': 'all', 'period': 'daily', 'rank': 1, 'period_stars': 123}])
        return repo

    def root(self, temporary):
        root = Path(temporary)
        (root / 'README.template.md').write_text((ROOT / 'README.template.md').read_text(encoding='utf-8'), encoding='utf-8')
        return root

    def test_realistic_card_entities_and_metrics(self):
        repo = parse_trending(CARD)[0]
        self.assertEqual(repo['name'], 'demo/llm-kit')
        self.assertEqual(repo['description'], 'A & B LLM toolkit. 中文简介')
        self.assertEqual((repo['stars'], repo['forks'], repo['period_stars']), (12345, 67, 123))
        self.assertEqual(repo['language'], 'Python')

    def test_blocked_or_changed_html_aborts(self):
        with self.assertRaises(ValueError):
            parse_trending('<html>Please sign in</html>')

    def test_language_url_encodes_cpp(self):
        self.assertEqual(trending_url('c++', 'daily'), 'https://github.com/trending/c%2B%2B?since=daily')

    def test_ai_word_boundaries_and_chinese(self):
        self.assertFalse(classify({'name': 'demo/email', 'description': 'A mailing and training tool'}, self.config))
        self.assertTrue(classify({'name': 'demo/tool', 'description': 'AI coding assistant'}, self.config))
        self.assertTrue(classify({'name': 'demo/tool', 'description': '本地大模型推理'}, self.config))

    def test_exclude_overrides_include(self):
        self.config.update(include_repositories=['Demo/Tool'], exclude_repositories=['demo/tool'])
        self.assertFalse(classify({'name': 'DEMO/tool', 'description': 'LLM'}, self.config))

    def test_deduplication_is_case_insensitive_and_survives_month_rollover(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = self.root(temporary)
            self.assertEqual(update_archive(root, '2026-12-31', [self.repo()], [], 1), 1)
            self.assertEqual(update_archive(root, '2027-01-01', [self.repo('Demo/LLM-kit')], [], 1), 0)
            self.assertTrue((root / 'archived/2026-12.md').exists())
            self.assertNotIn('[Demo/LLM-kit]', (root / 'README.md').read_text(encoding='utf-8'))
            records = read_json(root / 'data/repositories.json', {})['repositories']
            self.assertEqual(len(records), 1)
            self.assertEqual(records['demo/llm-kit']['first_seen'], '2026-12-31')
            self.assertEqual(records['demo/llm-kit']['last_seen'], '2027-01-01')

    def test_same_day_repeat_is_idempotent_and_merges_periods(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = self.root(temporary)
            update_archive(root, '2026-11-18', [self.repo()], ['daily'], 1)
            initial = {p.relative_to(root): p.read_bytes() for p in root.rglob('*') if p.is_file()}
            update_archive(root, '2026-11-18', [self.repo()], ['daily'], 1)
            self.assertEqual(initial, {p.relative_to(root): p.read_bytes() for p in root.rglob('*') if p.is_file()})
            weekly = self.repo()
            weekly['sources'][0]['period'] = 'weekly'
            update_archive(root, '2026-11-18', [weekly], ['weekly'], 1)
            snapshot = read_json(root / 'data/daily/2026-11-18.json', {})
            self.assertEqual(len(snapshot['repositories']), 1)
            self.assertEqual(len(snapshot['repositories'][0]['sources']), 2)

    def test_no_ai_matches_still_saves_snapshot(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = self.root(temporary)
            self.assertEqual(update_archive(root, '2026-11-18', [], ['source'], 25), 0)
            self.assertEqual(read_json(root / 'data/daily/2026-11-18.json', {})['repositories'], [])
            self.assertIn('No new projects this month.', (root / 'README.md').read_text(encoding='utf-8'))


if __name__ == '__main__':
    unittest.main()
