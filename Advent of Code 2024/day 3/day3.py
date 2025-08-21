import re

def part1(memory: str) -> int:
    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", memory)
    return sum(int(a) * int(b) for a, b in matches)

def part2(memory: str) -> int:
    tokens = re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)", memory)
    enabled = True
    total = 0
    for token in tokens:
        if token.group(0) == "do()":
            enabled = True
        elif token.group(0) == "don't()":
            enabled = False
        else:
            a, b = map(int, token.groups())
            if enabled:
                total += a * b
    return total

if __name__ == "__main__":
    with open("/Users/ethanclement/Documents/Advent of Code 2024/day 3/day3.txt", "r") as f:
        memory = f.read()

    print("Part 1:", part1(memory))
    print("Part 2:", part2(memory))
