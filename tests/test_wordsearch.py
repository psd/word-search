#!/usr/bin/env -S pytest -svv

import pytest
from wordsearch import WordSearcher


@pytest.fixture
def searcher():
    searcher = WordSearcher()
    searcher.load_words("tests/et.txt")
    searcher.score_letters()
    return searcher


def test_exclude(searcher):
    assert searcher.search(excludes="e") == {}
    assert list(searcher.search(excludes="h").keys()) == ["etude"]


def test_include_trumps_exclude(searcher):
    assert list(searcher.search(excludes="e", includes="eu").keys()) == ["etude"]
