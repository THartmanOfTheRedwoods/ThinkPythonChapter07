#!/usr/bin/env python3

from doctest import run_docstring_examples

def run_doctests(func):
    run_docstring_examples(func, globals(), name=func.__name__)

def uses_all(word, required):
    """Checks whether a word uses all required letters.

    >>> uses_all('banana', 'ban')
    True
    >>> uses_all('apple', 'api')
    False
    """
    required = required.lower()
    for l in word.lower():
        if l in required:
            required = required.replace(l, '')
        if len(required) == 0:
            return True
    return False

run_doctests(uses_all)