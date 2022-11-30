#!/bin/sh

# generate README from examples

cat <<-!
# Word search
[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/psd/word-search/blob/main/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://black.readthedocs.io/en/stable/)

Search a dictionary for words for wordle, duotrigortle etc
!

while read args
do
    cmd="python -m wordsearch $args"
    echo '```'
    echo $cmd
    echo
    eval $cmd
    echo '```'
    echo
done <<-!
--help

stare
stare log
stare log 'l[^o]'
-s
-p /usr/share/dict/words stare log 'l[^o]'
!
