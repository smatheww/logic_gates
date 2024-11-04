.PHONY: install test clean build

install:
	pip install -e .
	pip install -r requirements.txt

test:
	python -m pytest tests/ --cov=logic_gates

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type d -name "*.egg" -exec rm -rf {} +

build:
	python setup.py build