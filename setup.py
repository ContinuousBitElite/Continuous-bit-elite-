from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="continuous-bit-elite",
    version="4.0.14",
    author="ContinuousBitElite",
    author_email="continuous.bit.elite@gmail.com",
    description="Ultra-fast compression (3122x) with 4x ratio and blockchain integration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ContinuousBitElite/continuous-bit-elite",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Topic :: System :: Archiving :: Compression",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.24.0",
    ],
)
