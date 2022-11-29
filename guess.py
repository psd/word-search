#!/usr/bin/env python3

import sys
import re
import argparse


words = {}
letters = {}
letters_total = 0
places = {}


def ranked(dictionary):
    return sorted(dictionary.items(), key=lambda item: item[1], reverse=True)


def load(path):
    with open(path) as f:
        for word in f:
            words[word.strip().lower()] = 0

def score():
    global letters_total
    for word in words:
        place = 0
        for letter in word:
            letters.setdefault(letter, 0)
            letters[letter] += 1
            letters_total += 1

            places.setdefault(place, {})
            places[place].setdefault(letter, 0)
            places[place][letter] += 1
            place = place +1


def print_scores():
    for letter, count in ranked(letters):
        percent = round(count*100/letters_total)
        print(f"{letter}({percent}%) ", end='')

    print()
    for place in places:
        print(f"{place+1}: ", end="")
        for letter, count in ranked(places[place]):
            print(f"{letter}", end='')
        print()



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'Guess wordle, duotrigortle etc words')
    parser.add_argument('excludes', nargs="?", help="letters to exclude", type=str)
    parser.add_argument('includes', nargs="?", help="letters to include", type=str)
    parser.add_argument('match', nargs="?", help="regular expression to match", type=str)
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("-n", "--norepeat", help="guesses without repeating letters", action="store_true")
    parser.add_argument("-l", "--limit", help="limit the number of guesses", type=int, default=8)
    parser.add_argument("-p", "--path", help="path of words file", type=str, default="words")
    args = parser.parse_args()

    excludes = set(args.excludes or "")
    includes = set(args.includes or "")
    excludes = excludes - includes

    match = args.match
    limit = args.limit
    norepeat = args.norepeat
    verbose = args.verbose

    load(args.path)
    score()

    if args.verbose:
        print_scores()

    # best guesses scored on words on places
    found = {}
    for word in words:
        if excludes and (excludes & set(word)):
            continue

        if includes and (not (includes & set(word) == includes)):
            continue

        if match and not re.match(match, word):
            continue

        if norepeat and not len(set(word)) == len(word):
            continue

        place = 0
        score = 0
        used = []
        for letter in word:
            score += int((letters[letter]*2 + places[place][letter]) / word.count(letter))
            place += 1
        found[word] = score

    n=0
    for word, score in ranked(found):
        n = n + 1
        if n <= limit:
            if verbose:
                print(f"[{score}] ", end="")

            print(word)

    if verbose and n > limit:
        print("%d more ..." % (n-limit))
