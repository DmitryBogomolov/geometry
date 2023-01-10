init:
	pip3 install pylint
	pip3 install mypy

lint:
	@pylint geometry tests

check:
	@mypy .

test:
	@python3 -m unittest discover --verbose tests

.PHONY: init lint check
