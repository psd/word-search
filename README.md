usage: guess.py [-h] [-v] [-n] [-l LIMIT] [-p PATH]
                [excludes] [includes] [match]

Guess wordle, duotrigortle etc words

positional arguments:
  excludes              letters to exclude
  includes              letters to include
  match                 regular expression to match

options:
  -h, --help            show this help message and exit
  -v, --verbose
  -n, --norepeat        guesses without repeating letters
  -l LIMIT, --limit LIMIT
                        limit the number of guesses
  -p PATH, --path PATH  path of words file
