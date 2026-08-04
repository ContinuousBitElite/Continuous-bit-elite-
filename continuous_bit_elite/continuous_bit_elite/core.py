from setuptools import setup, find_packages

setup(
    name="continuous-bit-elite",
    version="4.0.2",  # ⬅️ إصدار جديد
    author="Continuous Bit Elite",
    author_email="continuous.bit.elite@gmail.com",
    description="Ultra-fast compression (3122×) with 4× ratio and blockchain integration",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ContinuousBitElite/Continuous-bit-elite-",
    packages=find_packages(),  # ⬅️ هذا سيجد جميع الملفات تلقائياً
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.24.0",
    ],
)
