from re import findall
from collections import Counter


def count_words(sentence):
    """Count how many times each word occurs in a sentence."""
    return Counter(findall("(?!')[a-z0-9']+(?<!')", sentence.lower()))
