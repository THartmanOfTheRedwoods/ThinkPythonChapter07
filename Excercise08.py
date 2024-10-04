#!/usr/bin/env python3

from doctest import run_docstring_examples

# AI IS HILARIOUS
# After a back and forth of Ping-Pong, Correct the ChatGPT Bot, if finally created this.
# Now this appears to work, but is absolutely ridiculous and inefficient.

def run_doctests(func):
    run_docstring_examples(func, globals(), name=func.__name__)

def uses_any(word, letters):
    """Checks if any of the letters in 'letters' are used in 'word'."""
    for letter in letters:
        if letter in word:
            return True
    return False

def uses_all(word, letters):
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
    for letter in letters:
        if not uses_any(word, letter):  # If any letter is not found in the word, return False
            return False
    return True

run_doctests(uses_all)