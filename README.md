# Word search

Search a dictionary for words for wordle, dutrigortle etc
```
python -m wordsearch --help

usage: word-search [-h] [-l LIMIT] [-n] [-p PATH] [-s] [-t]
                   [excludes] [includes] [match]

Search wordle, duotrigortle etc words

positional arguments:
  excludes              letters to exclude
  includes              letters to include
  match                 regular expression to match

options:
  -h, --help            show this help message and exit
  -l LIMIT, --limit LIMIT
                        limit the number of words
  -n, --norepeat        find words without repeating letters
  -p PATH, --path PATH  path of words file to search
  -s, --print-scores    print scores
  -t, --terse           only print the results
```

```
python -m wordsearch

stare
arose
irate
raise
arise
later
alter
slate
2307 more ...
```

```
python -m wordsearch stare

login
lingo
could
logic
cloud
nobly
cling
blond
219 more ...
```

```
python -m wordsearch stare log

login
lingo
logic
godly
ghoul
mogul
golly
igloo
1 more ...
```

```
python -m wordsearch stare log 'l[^o]'

lingo
```

```
python -m wordsearch -s

e (10.7%) a (8.5%) r (7.8%) o (6.5%) 
 t (6.3%) l (6.2%) i (5.8%) s (5.8%) 
 n (5.0%) c (4.1%) u (4.0%) y (3.7%) 
 d (3.4%) h (3.4%) p (3.2%) m (2.7%) 
 g (2.7%) b (2.4%) f (2.0%) k (1.8%) 
 w (1.7%) v (1.3%) z (0.3%) x (0.3%) 
 q (0.3%) j (0.2%) 

1: s (3.2%) c (1.7%) b (1.5%) t (1.3%) 
 p (1.2%) a (1.2%) f (1.2%) g (1.0%) 
 d (1.0%) m (0.9%) r (0.9%) l (0.8%) 
 w (0.7%) e (0.6%) h (0.6%) v (0.4%) 
 o (0.4%) n (0.3%) i (0.3%) u (0.3%) 
 q (0.2%) j (0.2%) k (0.2%) y (0.1%) 
 z (0.0%) 

2: a (2.6%) o (2.4%) r (2.3%) e (2.1%) 
 i (1.7%) l (1.7%) u (1.6%) h (1.2%) 
 n (0.8%) t (0.7%) p (0.5%) w (0.4%) 
 c (0.3%) m (0.3%) y (0.2%) d (0.2%) 
 b (0.1%) s (0.1%) v (0.1%) x (0.1%) 
 g (0.1%) k (0.1%) f (0.1%) q (0.0%) 
 z (0.0%) j (0.0%) 

3: a (2.7%) i (2.3%) o (2.1%) e (1.5%) 
 u (1.4%) r (1.4%) n (1.2%) l (1.0%) 
 t (1.0%) s (0.7%) d (0.6%) g (0.6%) 
 m (0.5%) p (0.5%) b (0.5%) c (0.5%) 
 v (0.4%) y (0.3%) w (0.2%) f (0.2%) 
 k (0.1%) x (0.1%) z (0.1%) h (0.1%) 
 j (0.0%) q (0.0%) 

4: e (2.7%) n (1.6%) s (1.5%) a (1.4%) 
 l (1.4%) i (1.4%) c (1.3%) r (1.3%) 
 t (1.2%) o (1.1%) u (0.7%) g (0.7%) 
 d (0.6%) m (0.6%) k (0.5%) p (0.4%) 
 v (0.4%) f (0.3%) h (0.2%) w (0.2%) 
 b (0.2%) z (0.2%) x (0.0%) y (0.0%) 
 j (0.0%) 

5: e (3.7%) y (3.1%) t (2.2%) r (1.8%) 
 l (1.3%) h (1.2%) n (1.1%) d (1.0%) 
 k (1.0%) a (0.6%) o (0.5%) p (0.5%) 
 m (0.4%) g (0.4%) s (0.3%) c (0.3%) 
 f (0.2%) w (0.1%) i (0.1%) b (0.1%) 
 x (0.1%) z (0.0%) u (0.0%) 

[10344] stare
[10315] arose
[10193] irate
[10172] raise
[10171] arise
[10151] later
[10101] alter
[10095] slate
2307 more ...
```

```
python -m wordsearch -p /usr/share/dict/words stare log 'l[^o]'

lionizing
lingo
```

