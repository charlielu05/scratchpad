SHELL := /bin/bash

python-env:
	rm -r .aips
	python -m venv .aips
	source .aips/bin/activate 
	pip-compile requirements.in --resolver=backtracking
	pip3 install --upgrade pip 
	pip3 install -r requirements.txt
	pip3 freeze > requirements.txt

python-test:
	source .aips/bin/activate
	python -m pytest tests/


.PHONY: *
.ONESHELL:
.SILENT: