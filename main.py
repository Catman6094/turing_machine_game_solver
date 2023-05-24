from itertools import product

CODES = list(product(range(1, 6), repeat=3))


def solve(puzzle):
    redundant = [True] * len(puzzle)
    solutions = []
    for a, b, c in CODES:
        wrong_clue = None   # Ends as a clue number if it's the ONLY clue that invalidates the code
        solution = True
        for i, f in enumerate(puzzle):
            if not f(a, b, c):
                if solution:
                    solution = False
                    wrong_clue = i
                else:
                    wrong_clue = None
                    break

        if solution:
            solutions.append((a, b, c))
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
    cards = [
        [
            lambda a, b, c: a < 3,
            lambda a, b, c: a == 3,
            lambda a, b, c: a > 3
        ], [
            lambda a, b, c: c % 3 == 0,
            lambda a, b, c: c % 3 == 1
        ], [
            lambda a, b, c: a < b and a < c,
            lambda a, b, c: b < a and b < c,
            lambda a, b, c: c < a and c < b
        ], [
            lambda a, b, c: [a, b, c].count(1) + [a, b, c].count(3) + [a, b, c].count(5) < [a, b, c].count(2) + [a, b, c].count(4),
            lambda a, b, c: [a, b, c].count(1) + [a, b, c].count(3) + [a, b, c].count(5) > [a, b, c].count(2) + [a, b, c].count(4)
        ]
    ]
    for puzzle, indices in zip(puzzle_iter(cards), product(*[range(len(c)) for c in cards])):
        solution = solve(puzzle)
        if solution: print(solution, indices)

if __name__ == "__main__":
    main()