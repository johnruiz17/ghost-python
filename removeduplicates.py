"""
File: removeduplicates.py
-------------------------
This program gives you practice with constructing a new list
based on values given to you by the user.  You also get
practice removing duplicates from that list
"""


def read_list():
    """
    This function should ask the user for a series of integer values
    (until the user enters 0 to stop) and store all those values in a
    list.  That list should then be returned by this function.
    """
    num_list = []

    # Prompts user to enter values. While loop stops when user enters 0.
    while True:
        num = int(input("Enter value (0 to stop) "))
        if num == 0:
            break
        else:
            num_list.append(num)

    return num_list


def remove_duplicates(num_list):
    """
    This function is passed a list of integers and returns a new
    list with all duplicate values from the original list remove.
    >>> remove_duplicates([1, 2, 3, 2, 3, 4])
    [1, 2, 3, 4]
    >>> remove_duplicates([1, 1, 1])
    [1]
    >>> remove_duplicates([])
    []
    """
    new_list = []

    # Iterate through list and make a new list. If number is not in new list, append it to the new list.
    for num in num_list:
        if num not in new_list:
            new_list.append(num)

    return new_list


def main():
    num_list = read_list()
    print("Original list entered by user: ")
    print(num_list)

    no_duplicates = remove_duplicates(num_list)
    print("List with duplicates removed: ")
    print(no_duplicates)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
