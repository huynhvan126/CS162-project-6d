# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 11/06/2024
# Description: Write a recursive function that takes a list of integers as a parameter and returns True if the puzzle is solvable for that row, but returns False otherwise.
def row_puzzle(row, index=0, memo=None):
    """
    Initialize memoization set if not provided
    """
    if memo is None:
        memo = set()

    if index == len(row) - 1:
        return True

    if index < 0 or index >= len(row) or index in memo:
        return False
   
    # Add the current index to memo to prevent revisiting.
    memo.add(index)

    # Value of the current index
    step = row[index]

    # Recursive calls to move left or right
    left_move = row_puzzle(row, index + step, memo)
    right_move = row_puzzle(row, index - step, memo)

    # If either move leads to the goal, return True
    return left_move or right_move
