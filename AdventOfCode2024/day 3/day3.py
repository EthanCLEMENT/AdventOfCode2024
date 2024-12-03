def read_file(prompt):  
    with open(prompt, "r") as file:
       content = file.read()
    return content

def problem1():
    import re

    pattern = r"mul\((\d+),(\d+)\)"

    content = read_file("/Users/ethanclement/Documents/AdventOfCode2024/day 3/day3.txt")

    matches = re.findall(pattern, content)

    ans =0
    for match in matches:
        x,y = map(int,match)
        product = x * y
        ans += product
    
    print(ans)

def problem2():
    import re

    mul_pattern = r"mul\((\d+),(\d+)\)"  
    do_pattern = r"do\(\)"               
    dont_pattern = r"don't\(\)"

    pattern = r"mul\((\d+),(\d+)\)"

    content = read_file("/Users/ethanclement/Documents/AdventOfCode2024/day 3/day3.txt")

    mul_enabled = True
    ans = 0

    tokens = re.split(r"(\bdo\(\)|\bdon't\(\)|mul\(\d+,\d+\))", content)

    for token in tokens:
        token = token.strip()
        if not token:
            continue

        if re.fullmatch(do_pattern, token):
            mul_enabled = True
        elif re.fullmatch(dont_pattern, token):
            mul_enabled = False
        elif mul_enabled and re.fullmatch(mul_pattern, token):
            x, y = map(int, re.findall(r"\d+", token))
            product = x * y
            ans += product
    print(ans)

problem1()
problem2()