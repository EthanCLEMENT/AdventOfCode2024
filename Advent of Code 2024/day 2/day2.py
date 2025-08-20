def read_file():

    rows = []
    with open("/Users/ethanclement/Documents/Advent of Code 2024/day 2/day2.txt", "r") as f:
        for line in f:
            rows.append(list(map(int, line.split())))

    return rows

def safe():
    data = read_file()
    count = 0

    for row in data:
        diffs = [row[i+1] - row[i] for i in range(len(row) - 1)]
        
        if all(1 <= d <= 3 for d in diffs) or all(-3 <= d <= -1 for d in diffs):
            count += 1

    return count

def safe_reactor():
    data = read_file()
    count = 0
    count_errors = 0
    for row in data:
        diffs = [row[i+1] - row[i] for i in range(len(row) - 1)]
        
        if sum(not (1 <= d <= 3) for d in diffs) <= 1 or sum(not (-3 <= d <= -1) for d in diffs) <= 1:
            count += 1


    return count


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


print(read_file())
print(safe())
print(safe_reactor())



