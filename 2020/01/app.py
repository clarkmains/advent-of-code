"""Advent of Code 2020 Day 1.

Part 1
------
Find the two entries that sum to 2020 and then multiply those two
numbers together. For example, suppose your expense report contained
the following:

1721
979
366
299
675
1456

In this list, the two entries that sum to 2020 are 1721 and 299.
Multiplying them together produces 1721 * 299 = 514579, so the correct
answer is 514579.

Part 2
------
The Elves in accounting are thankful for your help; one of them even
offers you a starfish coin they had left over from a past vacation. They
offer you a second one if you can find three numbers in your expense report
that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979,
366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum
to 2020?
"""


def read_expenses(expenses_file):
    with open(expenses_file) as f:
        return [int(expense) for expense in f]


def solve_part_1(expenses, target):
    result = None

    for expense in expenses:
        remainder = (target - expense)
        if remainder in expenses:
            result = expense * remainder
            break

    print(f"Part 1 Solution: {result}")


def solve_part_2(expenses, target):
    result = None

    for expense_1 in expenses:
        for expense_2 in expenses:
            remainder = (target - expense_1 - expense_2)
            if remainder in expenses:
                result = expense_1 * expense_2 * remainder
                break

    print(f"Part 2 Solution: {result}")


if __name__ == "__main__":
    expenses = read_expenses('expenses.txt')
    target = 2020

    solve_part_1(expenses, target)
    solve_part_2(expenses, target)
