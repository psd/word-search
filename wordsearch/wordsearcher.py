import re


def ranked(dictionary):
    return sorted(dictionary.items(), key=lambda item: item[1], reverse=True)


class WordSearcher:
    def __init__(self):
        self.words = {}
        self.letters = {}
        self.letters_count = 0
        self.places = {}

    def load_words(self, path):
        with open(path) as f:
            for word in f:
                self.words[word.strip().lower()] = 0

    def score_letters(self):
        for word in self.words:
            place = 0
            for letter in word:
                # count occurance of this letter
                self.letters.setdefault(letter, 0)
                self.letters[letter] += 1
                self.letters_count += 1

                # count occurance of this letter in this position
                self.places.setdefault(place, {})
                self.places[place].setdefault(letter, 0)
                self.places[place][letter] += 1
                place = place + 1

    def search(self, excludes="", includes="", match="", norepeat=False, occurance_factor=2, place_factor=1):
        excludes = set(excludes or "")
        includes = set(includes or "")
        excludes = excludes - includes

        found = {}
        for word in self.words:
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
            for letter in word:
                score += int(
                    (self.letters[letter] * occurance_factor + self.places[place][letter] * place_factor)
                    / word.count(letter)
                )
                place += 1
            found[word] = score

        return found

    def print_scored_letters(self, letters):
        n = 0
        for letter, count in ranked(letters):
            percent = count * 100.0 / float(self.letters_count)
            print(f"{letter} ({percent:.1f}%) ", end="")
            n = n + 1
            if 0 == n % 4:
                print("\n ", end="")
        print("\n")

    def print_scores(self):
        self.print_scored_letters(self.letters)

        for place, letters in self.places.items():
            print(f"{place+1}: ", end="")
            self.print_scored_letters(letters)

    def print_found(self, found, limit=8, print_scores=False, print_more=True):
        n = 0
        for word, score in ranked(found):
            n = n + 1
            if n <= limit:
                if print_scores:
                    print(f"[{score}] ", end="")

                print(word)

        if print_more:
            if n > limit:
                print("%d more ..." % (n - limit))
