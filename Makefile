.PHONY: lint test

lint:
	flake8 app tests

test:
	pytest tests