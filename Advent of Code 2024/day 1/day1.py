def read_file():

    rows = []
    with open("/Users/ethanclement/Documents/Advent of Code 2024/day 1/day1.txt", "r") as f:
        for line in f:
            rows.append(list(map(int, line.split())))

    return rows

def sorted_lists():
    return sorted(read_file(), key=lambda x: (x[0], x[1]))

def substract_lists():
    data = sorted_lists()

    left = sorted([row[0] for row in data])
    right = sorted([row[1] for row in data])

    total_distance = sum(abs(l - r) for l, r in zip(left, right))
    return total_distance

def score():
    from collections import Counter

    data = sorted_lists()

    left = sorted([row[0] for row in data])

    counter_rights = Counter([row[1] for row in data])
    
    return sum(i * counter_rights[i] for i in left)


print(sorted_lists())
print(substract_lists())
print(score())

