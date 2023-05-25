# Clues are represented as functions (tuple -> bool)
# Puzzles are lists of clues
# Verification Cards are also lists of clues
# Games are lists of cards

from itertools import product
from cards import *

CODES = list(product(range(1, 6), repeat=3))


def solve(puzzle):
    """Given a puzzle, return the solution code if it's unique and all clues are required, and return False otherwise
    """
    redundant = [True] * len(puzzle)
    solutions = []
    for c in CODES:
        wrong_clue = None   # Ends as a clue number if it's the ONLY clue that invalidates the code
        solution = True
        for i, f in enumerate(puzzle):
            if not f(c):
                if solution:
                    solution = False
                    wrong_clue = i
                else:
                    wrong_clue = None
                    break

        if solution:
            solutions.append(c)
            if len(solutions) > 1: return False
            
        if wrong_clue is not None:
            redundant[wrong_clue] = False
    
    if len(solutions) > 0 and not any(redundant):
        return solutions[0]
    return False


def puzzle_iter(cards):
    # Given criterion cards (lists of clues), loop through all puzzles (combinations of clues)
    for p in product(*cards):
        p = list(p)
        yield p


def main():
    cards = [C24, C26, C33, C42, C43]
    for puzzle, indices in zip(puzzle_iter(cards), product(*[range(len(c)) for c in cards])):
        solution = solve(puzzle)
        if solution: print(solution, indices)

if __name__ == "__main__":
    main()