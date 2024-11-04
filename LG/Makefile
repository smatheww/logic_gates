# Makefile for logic_gates.py project

.PHONY: all test lint clean

all: test lint

test:
	python3 -m unittest discover -s tests

lint:
	flake8 logic_gates.py

clean:
	rm -f *.pyc *.pyo __pycache__/*
