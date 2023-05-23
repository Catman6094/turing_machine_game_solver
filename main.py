from itertools import product

CODES = product(range(1, 6), repeat=3)


def is_good(puzzle):
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
    

c1 = lambda a, b, c: a == 1 and b == 2 and c == 3
c2 = lambda a, b, c: b == c
print(is_good([c1, c2]))