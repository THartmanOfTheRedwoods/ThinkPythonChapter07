#!/usr/bin/env python3

from doctest import run_docstring_examples
from Excercise03 import uses_only

def run_doctests(func):
    run_docstring_examples(func, globals(), name=func.__name__)

def uses_any(word, letters):
    for letter in word.lower():
        if letter in letters.lower():
            return True
    return False

def uses_none(word, forbidden):
    """Checks whether a word avoids forbidden letters.

    >>> uses_none('banana', 'xyz')
    True
    >>> uses_none('apple', 'efg')
    False
    >>> uses_none('', 'abc')
    True
    """
    return not uses_any( word, forbidden )

def uses_all(word, required):
    """Checks whether a word uses all required letters.

    >>> uses_all('banana', 'ban')
    True
    >>> uses_all('apple', 'api')
    False
    """
    # return uses_only(word, required) and len(set(word)) == len(required)
    return uses_only(required, word)

run_doctests(uses_all)
run_doctests(uses_none)