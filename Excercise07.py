#!/usr/bin/env python3

from doctest import run_docstring_examples

# AI IS HILARIOUS
# It solved the problem, but basically ignored my prompt about using the uses_only function, but id did write it ;-)
#
# "Given a function, uses_only, which takes two strings and checks that the first
# uses only the letters in the second, use it to write uses_all, which takes two
# strings and checks whether the first uses all the letters in the second,
# allowing repeats"

def run_doctests(func):
    run_docstring_examples(func, globals(), name=func.__name__)

def uses_only(word, allowed_letters):
    """Checks whether a word uses only the available letters.

    >>> uses_only('banana', 'ban')
    True
    >>> uses_only('apple', 'apl')
    False
    """
    for letter in word:
        if letter not in allowed_letters:
            return False
    return True

def uses_all(word, required_letters):
    """Checks whether a word uses all required letters.

    >>> uses_all('banana', 'ban')
    True
    >>> uses_all('apple', 'api')
    False
    >>> uses_all('hello', 'he')
    True
    >>> uses_all('hello', 'hey')
    False
    >>> uses_all('mississippi', 'miss')
    True
    """
    for letter in required_letters:
        if letter not in word:
            return False
    return True

run_doctests(uses_all)