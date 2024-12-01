def read_file(prompt):
    with open(prompt, 'r') as file : 
        arr = []
        for line in file :
            line_numbers  = list(map(int,line.split()))
            arr.append(line_numbers)
    return arr

def problem1() :
    prompt = '/Users/ethanclement/Documents/AdventOfCode2024/day 1/day1.txt'
    file = read_file(prompt)
    unzipped_lists = list(zip(*file))

    sorted_lists = []
    for lst in unzipped_lists:
        sorted_lists.append(sorted(lst))

    rezipped_lists = zip(*sorted_lists)

    sorted_arr = [list(x) for x in rezipped_lists]

    ans = 0

    for i in range(len(sorted_arr)): 
        for j in range(len(sorted_arr[i])):
            ans += abs(sorted_arr[i][0] - sorted_arr[i][j])
            print(ans)
    
    return 0

def problem2():
    prompt = '/Users/ethanclement/Documents/AdventOfCode2024/day 1/day1.txt'
    file = read_file(prompt)

    left_column_set = set()
    right_column = []
    
    for row in file:
        left_column_set.add(row[0])  
        right_column.append(row[1])  

    sorted_left_column = sorted(left_column_set)  
    sorted_right_column = sorted(right_column)

    counter = 0
    ans = 0

    for i in range(len(sorted_left_column)):
        for j in range(len(sorted_right_column)):
            if sorted_left_column[i] == sorted_right_column[j]:
                counter += 1
            else:
                ans += sorted_left_column[i] * counter
                counter = 0

    print(ans)
    return 0

    

    
problem1()
problem2()

