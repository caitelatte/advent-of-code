#!/usr/bin/env python

"""Advent of Code 2017 Day 4 - High-Entropy Passphrases

http://adventofcode.com/2017/day/4
"""

INPUT_FILENAME = "d04-input.txt"

if (__name__ == "__main__"):
    phrases = []
    # Take in input from file
    with (open(INPUT_FILENAME)) as f:
        for line in f:
            phrases.append(line)
    # Check for valid phrases
    valid_num = 0
    valid_anagrams = 0
    for p in phrases:
        is_valid = True
        is_anagram_valid = True
        p_words = set()
        p_words_sets = []
        for word in p.split():
            if word not in p_words:
                p_words.add(word)
            else:
                is_valid = False
                # print "The word {0} was in the set {1} - invalid!".format(word, p_words)
            if set(word) not in p_words_sets:
                p_words_sets.append(set(word))
            else:
                is_anagram_valid = False

        if is_valid:
            valid_num += 1
        if is_anagram_valid:
            valid_anagrams += 1
    # Return answer
    print "There are {0} valid whole word phrases in that input.".format(valid_num)
    print "There are {0} valid anagram word phrases in that input.".format(valid_anagrams)
