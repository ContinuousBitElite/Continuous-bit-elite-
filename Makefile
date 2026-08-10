.PHONY: help install install-dev test test-cov lint format clean build publish

help:
	@echo "Continuous Bit Elite - Development Commands"
	@echo ""
	@echo "Available commands:"
	@echo "  make install       Install the package"
	@echo "  make install-dev   Install with development dependencies"
	@echo "  make test          Run tests"
	@echo "  make test-cov      Run tests with coverage report"
	@echo "  make lint          Run linting checks"
	@echo "  make format        Format code with black and isort"
	@echo "  make clean         Clean build artifacts"
	@echo "  make build         Build distribution packages"
	@echo "  make publish       Publish to PyPI (requires credentials)"

install:
	pip install -e .

install-dev:
	pip install -e ".[dev]"

test:
	pytest tests/

test-cov:
	pytest tests/ --cov=continuous_bit_elite --cov-report=html --cov-report=term
	@echo "Coverage report generated in htmlcov/index.html"

lint:
	flake8 continuous_bit_elite tests/
	mypy continuous_bit_elite

format:
	black continuous_bit_elite tests/
	isort continuous_bit_elite tests/

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} +

test-clean: clean
	build: clean
	python -m build

publish: build
	python -m twine upload dist/*
