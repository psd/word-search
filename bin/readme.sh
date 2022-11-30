#!/bin/sh

# generate README from examples

cat <<-!
# Word search

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
