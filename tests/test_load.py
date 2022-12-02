#!/usr/bin/env -S pytest -svv

from wordsearch import WordSearcher


def test_load():
    searcher = WordSearcher()
    searcher.load_words("words")
    assert len(searcher.words) == 2315
