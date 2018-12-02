#! /usr/local/bin/python3
# Caitlin Macleod

"""AoC 2018 Day 2: Inventory Management System

Part one: 

What is the checksum for your list of box IDs?

Part two:

What letters are common between the two correct box IDs?

"""

def load_input(input_name):
    """Load the input file (a line-seperated list of numbers)."""
    with open(input_name) as input_file:
        input_list = []
        for line in input_file:
            input_list.append(line.strip())
    return input_list

def contains_dup_letters(word, n=2):
    """Check if a word has a letter which appears exactly 2 times."""
    letters = set(word)
    letters_counts = {}
    for letter in letters:
        letters_counts[letter] = word.count(letter)
    return (n in letters_counts.values())

def contains_two_letters(word):
    """Check if a word has a letter which appears 2 times."""
    return contains_dup_letters(word, 2)

def contains_three_letters(word):
    """Check if a word has a letter which appears 3 times."""
    return contains_dup_letters(word, 3)

def remove_nth_letter(word, n):
    """Return the word without the nth letter."""
    return (word[:n] + word[n+1:])

def find_duplicate(dup_list):
    seen = set()
    for x in dup_list:
        if x in seen:
            return x
        else:
            seen.add(x)

if __name__ == "__main__":
    box_list = load_input("d02-input.txt")

    # Find answer 1: a checksum
    two_of_letter_list = list(filter(contains_two_letters, box_list))
    three_of_letter_list = list(filter(contains_three_letters, box_list))
    checksum = (len(two_of_letter_list) * len(three_of_letter_list))
    print(f"The checksum for this list is {checksum}: {len(two_of_letter_list)} * {len(three_of_letter_list)}.")

    # Find answer 2: the correct boxids.
    # print(f"removed 2nd letter from {box_list[0]} to make {remove_nth_letter(box_list[0], 25)}")
    # Check each position for duplicate entries
    duplicate = None
    for index in range(len(box_list[0])):
        removed_list = [remove_nth_letter(x, index) for x in box_list]
        if len(set(removed_list)) < len(box_list):
            duplicate = find_duplicate(removed_list)
            break
    print(f"The common letters in the duplicate box id are: {duplicate}")