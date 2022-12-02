.PHONY: init all lint test

SOURCE=$(wildcard wordsearch/*.py)

all:: lint test README.md

test::
	pytest --cov=./ --cov-report=xml

lint::
	black --check $(SOURCE)
	flake8 $(SOURCE)

black::
	black $(SOURCE)

README.md: $(SOURCE) bin/readme.sh
	bin/readme.sh > $@

init::
	pip install -e .[test]
