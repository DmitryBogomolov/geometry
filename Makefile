init:
	pip3 install pylint
	pip3 install mypy

lint:
	@pylint *.py

check:
	@mypy .

.PHONY: init lint check
