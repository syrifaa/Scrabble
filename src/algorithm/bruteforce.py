from itertools import permutations

def bruteforce_match(chars, indexChar, rack_letters):
    combinations = []

    length = len(rack_letters)
    for perm in permutations(chars, length):
        if filter_combinations("".join(perm), indexChar):
            combinations.append("".join(perm))
   
    # print(combinations)
    return combinations

def filter_combinations(combinations, indexChar):
    count = 0
    for j in range(len(combinations)):
        for k in range(len(indexChar)):
            if j == indexChar[k][1] and combinations[j] == indexChar[k][0]:
                count += 1
    return count == len(indexChar)