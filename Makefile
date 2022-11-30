.PHONY: init all lint test

SOURCE=$(wildcard wordsearch/*.py)

all:: lint test README.md

test::
	:

lint::
	black --check $(SOURCE)
	flake8 $(SOURCE)

README.md: $(SOURCE) bin/readme.sh
	bin/readme.sh > $@

init::
	pip3 install -r requirements.txt
