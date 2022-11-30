.PHONY: init all lint test

all:: lint test

test::
	:

lint::
	black --check *.py
	flake8 *.py

init::
	pip3 install -r requirements.txt
