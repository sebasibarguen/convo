import pytest


@pytest.fixture
def matcher():
    """ Pytest fixture for matcher """
    from fuzzy_match import FuzzyMatcher
    matcher = FuzzyMatcher()
    yield matcher


@pytest.mark.parametrize(('keyword', 'suggestion'), (
    ('hool', 'tool'),
    ('chool', 'school'),
    ('schoo', 'school'),
    ('grammr', 'grammar'),
    ('homm', 'home'),
    ('homee', 'home'),
    ('yuo', 'you'),
))
def test_keyword_match(matcher, keyword, suggestion):
    response = matcher.match(keyword)
    res_suggestions = [s[1] for s in response]
    assert suggestion in res_suggestions