import os
import sys

from setuptools import find_packages, setup


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="word-search",
    version="0.1",
    description="Search a dictionary for the words containing a set of letters, useful for crosswords, wordle, duotrigortle etc",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Paul Sumner Downey (psd)",
    author_email="psd@whatfettle.com",
    license="MIT",
    url="https://github.com/psd/word-search",
    packages=find_packages(exclude="tests"),
    package_data={"word-search": ["words"]},
    include_package_data=True,
    install_requires=[],
    entry_points={"console_scripts": ["word-search=wordsearch.__main__:main"]},
    setup_requires=["pytest-runner"],
    extras_require={
        "test": [
            "black",
            "coverage",
            "coveralls",
            "flake8",
            "flake8-pyproject",
            "pytest",
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Text Processing :: Filters",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
    ],
)
