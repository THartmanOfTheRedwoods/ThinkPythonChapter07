#!/usr/bin/env python3

from doctest import run_docstring_examples

def run_doctests(func):
    run_docstring_examples(func, globals(), name=func.__name__)

def uses_none(word, forbidden):
    """Checks whether a word avoid forbidden letters.

    >>> uses_none('banana', 'xyz')
    True
    >>> uses_none('apple', 'efg')
    False
    """
    word = word.lower()
    for l in forbidden.lower():
        if l in word:
            return False
    return True

run_doctests(uses_none)