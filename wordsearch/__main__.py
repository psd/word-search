#!/usr/bin/env python3

import argparse
from .wordsearcher import WordSearcher


if __name__ == "__main__":
    parser = argparse.ArgumentParser("word-search", description="Search wordle, duotrigortle etc words")
    parser.add_argument("excludes", nargs="?", help="letters to exclude", type=str)
    parser.add_argument("includes", nargs="?", help="letters to include", type=str)
    parser.add_argument("match", nargs="?", help="regular expression to match", type=str)
    parser.add_argument("-l", "--limit", help="limit the number of words", type=int, default=8)
    parser.add_argument("-n", "--norepeat", help="find words without repeating letters", action="store_true")
    parser.add_argument("-p", "--path", help="path of words file to search", type=str, default="words")
    parser.add_argument("-s", "--print-scores", help="print scores", action="store_true")
    parser.add_argument("-t", "--terse", help="only print the results", action="store_true")
    args = parser.parse_args()

    searcher = WordSearcher()
    searcher.load_words(args.path)
    searcher.score_letters()

    if args.print_scores:
        searcher.print_scores()

    found = searcher.search(args.excludes, args.includes, args.match, args.norepeat)
    searcher.print_found(found, print_scores=args.print_scores, print_more=not args.terse)
