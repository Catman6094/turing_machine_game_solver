C2 = [
    lambda c: c[0] < 3,
    lambda c: c[0] == 3,
    lambda c: c[0] > 3
]

C7 = [
    lambda c: c[2] % 2 == 0,
    lambda c: c[2] % 2 == 1,
]

C8 = [
    lambda c: c.count(1) == 0,
    lambda c: c.count(1) == 1,
    lambda c: c.count(1) == 2,
    lambda c: c.count(1) == 3
]

C9 = [
    lambda c: c.count(3) == 0,
    lambda c: c.count(3) == 1,
    lambda c: c.count(3) == 2,
    lambda c: c.count(3) == 3
]

C10 = [
    lambda c: c.count(4) == 0,
    lambda c: c.count(4) == 1,
    lambda c: c.count(4) == 2,
    lambda c: c.count(4) == 3
]

C11 = [
    lambda c: c[0] < c[1],
    lambda c: c[0] == c[1],
    lambda c: c[0] > c[1],
]

C13 = [
    lambda c: c[1] < c[2],
    lambda c: c[1] == c[2],
    lambda c: c[1] > c[2]
]

C15 = [
    lambda c: c[0] > c[1] and c[0] > c[2],
    lambda c: c[1] > c[0] and c[1] > c[2],
    lambda c: c[2] > c[0] and c[2] > c[1]
]

C16 = [
    lambda c: (lambda x: x.count(0) >= 2)((c[0] % 2, c[1] % 2, c[2] % 2)),
    lambda c: (lambda x: x.count(0) <= 1)((c[0] % 2, c[1] % 2, c[2] % 2))
]

C17 = [
    lambda c: (lambda x: x.count(0) == 0)((c[0] % 2, c[1] % 2, c[2] % 2)),
    lambda c: (lambda x: x.count(0) == 1)((c[0] % 2, c[1] % 2, c[2] % 2)),
    lambda c: (lambda x: x.count(0) == 2)((c[0] % 2, c[1] % 2, c[2] % 2)),
    lambda c: (lambda x: x.count(0) == 3)((c[0] % 2, c[1] % 2, c[2] % 2))
]

C18 = [
    lambda c: sum(c) % 2 == 0,
    lambda c: sum(c) % 2 == 1
]

C19 = [
    lambda c: c[0] + c[1] < 6,
    lambda c: c[0] + c[1] == 6,
    lambda c: c[0] + c[1] > 6,
]

C20 = [
    lambda c: len(set(c)) == 1,
    lambda c: len(set(c)) == 2,
    lambda c: len(set(c)) == 3
]

C22 = [
    lambda c: c[0] < c[1] < c[2],
    lambda c: c[0] > c[1] > c[2],
    lambda c: not ((c[0] < c[1] < c[2]) or (c[0] > c[1] > c[2]))
]

C24 = [
    lambda c: int(c[0] + 1 == c[1]) + int(c[1] + 1 == c[2]) == 2,
    lambda c: int(c[0] + 1 == c[1]) + int(c[1] + 1 == c[2]) == 1,
    lambda c: int(c[0] + 1 == c[1]) + int(c[1] + 1 == c[2]) == 0
]

C26 = [
    lambda c: c[0] < 3,
    lambda c: c[1] < 3,
    lambda c: c[2] < 3
]

C33 = [
    lambda c: c[0] % 2 == 0,
    lambda c: c[1] % 2 == 0,
    lambda c: c[2] % 2 == 0,
    lambda c: c[0] % 2 == 1,
    lambda c: c[1] % 2 == 1,
    lambda c: c[2] % 2 == 1
]

C42 = [
    lambda c: c[0] < c[1] and c[0] < c[2],
    lambda c: c[1] < c[0] and c[1] < c[2],
    lambda c: c[2] < c[0] and c[2] < c[1],
    lambda c: c[0] > c[1] and c[0] > c[2],
    lambda c: c[1] > c[0] and c[1] > c[2],
    lambda c: c[2] > c[0] and c[2] > c[1]
]

C43 = [
    lambda c: c[0] < c[1],
    lambda c: c[0] == c[1],
    lambda c: c[0] > c[1],
    lambda c: c[0] < c[2],
    lambda c: c[0] == c[2],
    lambda c: c[0] > c[2]
]