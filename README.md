# guess words

	$ ./guess.py --help

	usage: guess.py [-h] [-l LIMIT] [-n] [-p PATH] [-s] [-t]
			[excludes] [includes] [match]

	Guess words in a dictionary, useful for wordle, duotrigortle etc

	positional arguments:
	  excludes              letters to exclude
	  includes              letters to include
	  match                 regular expression to match

	options:
	  -h, --help            show this help message and exit
	  -l LIMIT, --limit LIMIT
				limit the number of guesses
	  -n, --norepeat        guesses without repeating letters
	  -p PATH, --path PATH  path of words file
	  -s, --print-scores    print scores
	  -t, --terse           only print the results


	$ ./guess.py
	stare
	arose
	irate
	raise
	arise
	later
	alter
	slate
	2307 more ...


	$ ./guess.py stare
	login
	lingo
	could
	logic
	cloud
	nobly
	cling
	blond
	219 more ...


	$ ./guess.py stare logi
	login
	lingo
	logic
	igloo


	$ ./guess.py iertgin saol 's[^a]'
	shoal


        $ ./word-guess.py -s
	e (10.7%) a (8.5%) r (7.8%) o (6.5%) 
	 t (6.3%) l (6.2%) i (5.8%) s (5.8%) 
	 n (5.0%) c (4.1%) u (4.0%) y (3.7%) 
	 d (3.4%) h (3.4%) p (3.2%) m (2.7%) 
	 g (2.7%) b (2.4%) f (2.0%) k (1.8%) 
	 w (1.7%) v (1.3%) z (0.3%) x (0.3%) 
	 q (0.3%) j (0.2%) 
	1: scbtpafgdmrlwehvoniuqjkyz
	2: aoreiluhntpwcmydbsvxgkfqzj
	3: aioeurnltsdgmpbcvywfkxzhjq
	4: ensalicrtougdmkpvfhwbzxyj
	5: eytrlhndkaopmgscfwibxzu
	[10344] stare
	[10315] arose
	[10193] irate
	[10172] raise
	[10171] arise
	[10151] later
	[10101] alter
	[10095] slate
	2307 more ...
