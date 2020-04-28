from unittest import TestCase, mock

from fuzzy_match import FuzzyMatcher


class TestFuzzyMatcher(TestCase):

    def setUp(self):
        self.matcher = FuzzyMatcher()

    def test_matcher(self):
        keyword = 'chool'
        suggestions = self.matcher.match(keyword)
        suggested_words = [s[1] for s in suggestions]
        assert 'school' == suggested_words[0]