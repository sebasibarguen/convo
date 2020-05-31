"""
Author: Peter Norvig

https://norvig.com/spell-correct.html
"""

import pytest

from collections import Counter

@pytest.fixture
def spell():
    """ Pytest fixture for matcher """
    from convo.spellchecker import spell
    yield spell

def test_correction(spell):
    assert spell.correction('speling') == 'spelling'              # insert
    assert spell.correction('korrectud') == 'corrected'           # replace 2
    assert spell.correction('bycycle') == 'bicycle'               # replace
    assert spell.correction('inconvient') == 'inconvenient'       # insert 2
    assert spell.correction('arrainged') == 'arranged'            # delete
    assert spell.correction('peotry') =='poetry'                  # transpose
    assert spell.correction('peotryy') =='poetry'                 # transpose + delete
    assert spell.correction('word') == 'word'                     # known
    assert spell.correction('quintessential') == 'quintessential' # unknown


def test_p(spell):
    assert spell.P('quintessential') == 0
    assert 0.07 < spell.P('the') < 0.08


def test_words(spell):
    assert spell.words('This is a TEST.') == ['this', 'is', 'a', 'test']
    assert Counter(spell.words('This is a test. 123; A TEST this is.')) == (
        Counter({'123': 1, 'a': 2, 'is': 2, 'test': 2, 'this': 2}))


def test_word_dict(spell):
    assert spell.WORDS.most_common(10) == [
     ('the', 79809),
     ('of', 40024),
     ('and', 38312),
     ('to', 28765),
     ('in', 22023),
     ('a', 21124),
     ('that', 12512),
     ('he', 12401),
     ('was', 11410),
     ('it', 10681)]
    assert spell.WORDS['the'] == 79809
    assert len(spell.WORDS) == 32198
    assert sum(spell.WORDS.values()) == 1115585