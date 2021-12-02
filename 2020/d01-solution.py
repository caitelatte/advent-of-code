#! /usr/local/bin/python3
# Caitlin M

def load_input(input_name):
    """Load the input file (a line-seperated list of numbers)."""
    with open(input_name) as input_file:
        input_list = []
        for line in input_file:
            input_list.append(int(line.strip()))
    return input_list

if __name__ == "__main__":
    expenses = load_input("d01-input.txt")

    for expense in expenses:
        for other_expense in expenses:
            if (expense + other_expense == 2020):
                print(f"the good numbers are {expense} and {other_expense} and multiplied they make {expense*other_expense}")

    sorted_expenses = sorted(expenses)

    for expense in sorted_expenses:
        for other_expense in sorted_expenses:
            if (expense + other_expense > 2020):
                break
            for other_other_expense in sorted_expenses:
                if (expense + other_expense + other_other_expense > 2020):
                    break
                if (expense + other_expense + other_other_expense == 2020):
                    print(f"the three good numbers are {(expense, other_expense, other_other_expense)} and they multiply to {expense*other_expense*other_other_expense}")
