#!/usr/bin/env python3

from doctest import run_docstring_examples

def run_doctests(func):
    run_docstring_examples(func, globals(), name=func.__name__)

def uses_only(word, available):
    """Checks whether a word uses only the available letters.

    >>> uses_only('banana', 'ban')
    True
    >>> uses_only('apple', 'apl')
    False
    """
    available = available.lower()
    for l in word.lower():
        if l not in available:
            return False
    return True

run_doctests(uses_only)