#!/usr/bin/env -S pytest -svv

from wordsearch import WordSearcher


def test_load():
    searcher = WordSearcher()
    searcher.load_words()
    assert len(searcher.words) == 2315
