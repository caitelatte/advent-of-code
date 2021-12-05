#! /usr/local/bin/python3
# Caitlin M

"""AoC Day 4: Giant Squid

Original problem at https://adventofcode.com/2021/day/4

"""

BINGO_SIZE = 5

def mark_bingo_boards(bingo_num):
    """Replace specified number with X in all boards"""
    global bingoboards
    for board in bingoboards:
        for line in board:
            try:
                line[line.index(bingo_num)] = "X"
            except ValueError:
                pass

def check_bingo_board(board_num):
    """Check a bingo board for 5 Xs in a row"""
    winning_board = False
    for i in range(BINGO_SIZE):
        if bingoboards[board_num][i].count("X") == 5:
            winning_board = board_num
    for j in range(BINGO_SIZE):
        col = list(map(lambda x: x[j], bingoboards[board_num]))
        if col.count("X") == 5:
            winning_board = board_num
    return winning_board
            
def count_bingo_board(board_num):
    """Count score of a winning board"""
    bingo_score = 0
    for row in bingoboards[board_num]:
        bingo_score += sum(list(filter(lambda x: x != "X", row)))
    return bingo_score

def load_input(input_name):
    """Load the input file (a line-seperated list of numbers)."""
    with open(input_name) as input_file:
        bingonumbers = list(map(int, input_file.readline().split(",")))
        boards = []
        board_num = -1
        board_row = -1
        for line in input_file.readlines():
            if line.strip() == "":
                board_num += 1
                board_row = -1
                boards.append([])
            else:
                boards[board_num].append(list(map(int, line.split())))
    return (bingonumbers, boards)

if __name__ == "__main__":
    (bingonumbers, bingoboards) = load_input("d04-input.txt")
    all_winners = []
    winning_board = False
    winning_score = 0
    for bingo_num in bingonumbers:
        mark_bingo_boards(bingo_num)
        for board_num in range(len(bingoboards)):
            if check_bingo_board(board_num) and board_num not in all_winners:
                winning_board = board_num
                winning_score = count_bingo_board(board_num) * bingo_num
                all_winners.append(winning_board)
                print(f"the winner is {winning_board} {bingoboards[winning_board]} with a score of {winning_score}")
                if len(bingoboards) == 0:
                    break