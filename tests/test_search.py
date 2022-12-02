#!/usr/bin/env -S pytest -svv

import pytest
from wordsearch import WordSearcher


@pytest.fixture
def searcher():
    searcher = WordSearcher()
    searcher.load_words("tests/et.txt")
    searcher.score_letters()
    return searcher


def test_all(searcher):
    assert sorted(searcher.search().keys()) == ['ether', 'ethic', 'ethos', 'etude']


def test_exclude(searcher):
    assert searcher.search(excludes="e") == {}
    assert list(searcher.search(excludes="h").keys()) == ["etude"]


def test_include(searcher):
    assert searcher.search(includes="xyz") == {}
    assert sorted(searcher.search(includes="u").keys()) == ["etude"]
    assert sorted(searcher.search(includes="eth").keys()) == ['ether', 'ethic', 'ethos']


def test_intersection(searcher):
    assert sorted(searcher.search(excludes="e", includes="eu").keys()) == ["etude"]


def test_match(searcher):
    assert sorted(searcher.search(match=".*c")) == ["ethic"]
    assert sorted(searcher.search(match="e...c")) == ["ethic"]
    assert sorted(searcher.search(match="...e")) == ["ether"]


def test_norepeat(searcher):
    assert sorted(searcher.search(norepeat=True).keys()) == ['ethic', 'ethos']


