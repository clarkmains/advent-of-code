"""Find the two entries that sum to 2020 and then multiply those two numbers
together. For example, suppose your expense report contained the following:

1721
979
366
299
675
1456

In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying
them together produces 1721 * 299 = 514579, so the correct answer is 514579.
"""


def main(expenses_file, target):
    matches = None

    with open(expenses_file) as f:
        expenses = f.read().splitlines()

    for index, expense in enumerate(expenses):
        remainder = target - int(expense)
        
        try:
            remainder_index = expenses.index(str(remainder))
        except ValueError:
            continue
        else:
            if index != remainder_index:
                matches = (int(expense), remainder)
                break

    if matches:
        print(f"The result is {matches[0] * matches[1]}")
    else:
        print(f"Sorry - I didn't find two numbers that sum to {str(target)}")


if __name__ == "__main__":
    main(expenses_file='expenses.txt', target=2020)
