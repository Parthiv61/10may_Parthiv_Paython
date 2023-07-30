""" Write a Python function that takes a list of words and returns the length 
of the longest one."""

def longest_word(words):
    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
    