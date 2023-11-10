SHELL=/bin/bash

.PHONY: code-coverage
code-coverage:
	python3 -m coverage run -m unittest
	python3 -m coverage html
	firefox htmlcov/index.html

.PHONY: lint-python
lint-python:
	# Ignore TODOs and short variable names like zi (字)
	pylint --disable=fixme,invalid-name src/guangyun.py

.PHONY: clean
clean:
	rm -rf htmlcov
