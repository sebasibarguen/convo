import os
import json

import pytest

FIXTURE_FILE_PATH = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'word_permutations.json')
permutation_fixtures = json.loads(open(FIXTURE_FILE_PATH, 'r').read())


@pytest.fixture
def matcher():
    """ Pytest fixture for matcher """
    from spellchecker import word_permutations as matcher
    yield matcher


def test_permutate_x(matcher):
    word = 'x'
    distance = 1
    permutations = permutation_fixtures[word]

    response = matcher.permutate_word(word, distance)
    assert response == set(permutations)


def test_permutate_chool(matcher):
    word = 'chool'
    distance = 1
    permutations = permutation_fixtures[word]

    response = matcher.permutate_word(word, distance)
    assert response == set(permutations)