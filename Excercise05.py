#!/usr/bin/env python3

from doctest import run_docstring_examples
from Excercise03 import uses_only
from Excercise04 import uses_all

def run_doctests(func):
    run_docstring_examples(func, globals(), name=func.__name__)

def check_word(word, available, required):
    """Check whether a word is acceptable.

    >>> check_word('color', 'ACDLORT', 'R')
    True
    >>> check_word('ratatat', 'ACDLORT', 'R')
    True
    >>> check_word('rat', 'ACDLORT', 'R')
    False
    >>> check_word('told', 'ACDLORT', 'R')
    False
    >>> check_word('bee', 'ACDLORT', 'R')
    False
    """
    if len(word) < 4: return False
    word = word.lower()
    if not required.lower() in word: return False
    return uses_only(word, available)


def word_score(word, available):
    """Compute the score for an acceptable word.

    >>> word_score('card', 'ACDLORT')
    1
    >>> word_score('color', 'ACDLORT')
    5
    >>> word_score('cartload', 'ACDLORT')
    15
    """
    score = len(word) if len(word) > 4 else 1
    if uses_all(word, available): score += 7
    return score

run_doctests(check_word)
run_doctests(word_score)