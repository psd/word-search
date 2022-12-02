#!/usr/bin/env -S pytest -svv

from wordsearch import WordSearcher


def test_score_letters():
    searcher = WordSearcher()

    searcher.load_words("tests/et.txt")
    assert len(searcher.words) == 4
    searcher.words = ["ether", "ethic", "ethos", "etude"]

    searcher.score_letters()

    assert searcher.letters_count == 20
    assert ''.join(sorted(searcher.letters.keys())) == 'cdehiorstu'

    assert searcher.places[0] == { 'e': 4 }
    assert searcher.places[1] == { 't': 4 }
    assert searcher.places[2] == { 'h': 3, 'u': 1 }
    assert searcher.places[3] == { 'e': 1, 'i': 1, 'o': 1, 'd': 1 }
    assert searcher.places[4] == { 'r': 1, 'c': 1, 's': 1, 'e': 1  }
