#!/usr/bin/env python3

from sys import argv
import re

words = {}
letters = {}
letters_total = 0
places = {}


def ranked(dictionary):
    return sorted(dictionary.items(), key=lambda item: item[1], reverse=True)


def load():
    with open("words") as f:
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
        percent = round(count*1000/letters_total)
        print(f"{letter}({percent}) ", end='')

    print()
    for place in places:
        for letter, count in ranked(places[place]):
            print(f"{letter}", end='')
        print()


load()
score()

#print_scores()

excludes = set(argv[1] if len(argv) > 1 else "")
includes = set(argv[2] if len(argv) > 2 else "")
match = argv[3] if len(argv) > 3 else None
norepeat = len(argv) > 4

excludes = excludes - includes

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
        score += (letters[letter]*2 + places[place][letter]) / word.count(letter)
        place += 1
    found[word] = score

n=0
for word, score in ranked(found):
    print(word)
    n = n + 1
    if n > 8:
        print("...")
        break
