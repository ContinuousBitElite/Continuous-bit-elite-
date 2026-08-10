# Contributing to Continuous Bit Elite

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing.

## Code of Conduct

This project adheres to the Contributor Covenant [code of conduct](./CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in [Issues](https://github.com/ContinuousBitElite/Continuous-bit-elite-/issues)
2. If not, create a new issue with:
   - Clear, descriptive title
   - Detailed description of the bug
   - Steps to reproduce
   - Expected vs actual behavior
   - Python version and OS
   - Any relevant error messages

### Suggesting Enhancements

1. Check if the enhancement has been suggested
2. Create an issue with:
   - Clear, descriptive title
   - Detailed description
   - Use cases and benefits
   - Possible implementation ideas (optional)

### Pull Requests

1. **Fork the repository**
   ```bash
   git clone https://github.com/YOUR-USERNAME/Continuous-bit-elite-.git
   cd Continuous-bit-elite-
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Write clean, readable code
   - Follow PEP 8 style guidelines
   - Add tests for new features
   - Update documentation as needed

4. **Run tests locally**
   ```bash
   pytest tests/
   ```

5. **Commit your changes**
   ```bash
   git commit -m "Add your descriptive commit message"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**
   - Describe what you changed and why
   - Reference any related issues
   - Ensure all tests pass

## Development Setup

### Requirements
- Python 3.8+
- pip or conda

### Installation
```bash
# Clone the repository
git clone https://github.com/ContinuousBitElite/Continuous-bit-elite-.git
cd Continuous-bit-elite-

# Install in development mode
pip install -e .

# Install development dependencies
pip install pytest pytest-cov
```

### Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=continuous_bit_elite tests/

# Run specific test file
pytest tests/test_compression.py
```

## Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use type hints when possible
- Write docstrings for functions and classes
- Maximum line length: 100 characters

## Commit Messages

- Use clear, descriptive messages
- Start with a verb (Add, Fix, Update, Remove, etc.)
- Reference issues when relevant
- Example: `Fix compression parameter handling in decompress()`

## Questions?

Feel free to open an issue or contact the maintainers. We're here to help!

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
