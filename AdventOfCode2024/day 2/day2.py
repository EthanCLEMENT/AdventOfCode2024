def read_file(prompt):
    with open(prompt, 'r') as file : 
        arr = []
        for line in file :
            line_numbers  = list(map(int,line.split()))
            arr.append(line_numbers)
    return arr

def problem1():
    prompt = '/Users/ethanclement/Documents/AdventOfCode2024/day 2/day2.txt'
    file = read_file(prompt)

    ans = 0

    for sublist in file:
        is_valid = True  

        for j in range(len(sublist) - 1):
            if not (1 <= abs(sublist[j] - sublist[j + 1]) <= 3):
                is_valid = False
                break

        if is_valid:
            is_increasing = all(sublist[k] <= sublist[k + 1] for k in range(len(sublist) - 1))
            is_decreasing = all(sublist[k] >= sublist[k + 1] for k in range(len(sublist) - 1))
            if not (is_increasing or is_decreasing):
                is_valid = False

        if is_valid:
            ans += 1

    print(ans)

def problem2():
    prompt = '/Users/ethanclement/Documents/AdventOfCode2024/day 2/day2.txt'
    file = read_file(prompt)

    ans = 0
    
    for sublist in file:
        if is_safe(sublist):
            ans += 1
            continue

        for i in range(len(sublist)):
            modified_sublist = sublist[:i] + sublist[i+1:]
            if is_safe(modified_sublist):
                ans += 1
                break  

    print(ans)
    
def is_safe(sublist):
    if not sublist:
        return False 

    increasing = all(sublist[i] < sublist[i+1] and 1 <= sublist[i+1] - sublist[i] <= 3 for i in range(len(sublist)-1))
    decreasing = all(sublist[i] > sublist[i+1] and 1 <= sublist[i] - sublist[i+1] <= 3 for i in range(len(sublist)-1))

    return increasing or decreasing

problem1()
problem2()