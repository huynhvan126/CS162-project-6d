# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 11/06/2024
# Description: Write a recursive function that takes a list of integers as a parameter and returns True if the puzzle is solvable for that row, but returns False otherwise.
def row_puzzle(row, index=0, visited=set()):
    """
    This function checks if a puzzle represented by a row of numbers is solvable.
    """
    if index == len(row) - 1:
        return True
    if index in visited:
        return False

    # Try moving left and right.
    visited.add(index)
    left_move = index - row[index] if index - row[index] >= 0 else None
    right_move = index + row[index] if index + row[index] < len(row) else None

    # Check if either move leads to a solution
    solution = False
    if left_move is not None:
        solution = row_puzzle(row.copy(),left_move, visited.copy())
    if not solution and right_move is not None:
        solution = row_puzzle(row.copy(),right_move, visited.copy())

    # Remove the index from visited before returning
    visited.remove(index)
    return solution