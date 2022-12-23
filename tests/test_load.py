#!/usr/bin/env -S pytest -svv

import pytest
from wordsearch import WordSearcher


def test_load_package():
    searcher = WordSearcher()

    searcher.load_words("words")
    assert len(searcher.words) == 2315


def test_load_path():
    searcher = WordSearcher()

    searcher.load_words("tests/ab.txt")
    assert len(searcher.words) == 14

    searcher.load_words("tests/et.txt")
    assert len(searcher.words) == 18
