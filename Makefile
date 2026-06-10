.PHONY: test run all

all: test run

test:
	python -m unittest discover -s tests

run:
	python api/gateway.py
