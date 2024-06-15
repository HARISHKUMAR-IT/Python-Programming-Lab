Give a dictionary with value lists, sort the keys by summation of values in value list.

 Input : test_dict = {‘Gfg’ : [6, 7, 4], ‘best’ : [7, 6, 5]}

Output : {‘Gfg’: 17, ‘best’: 18}

Explanation : Sorted by sum, and replaced.

 Input : test_dict = {‘Gfg’ : [8,8], ‘best’ : [5,5]}

Output : {‘best’: 10, ‘Gfg’: 16}

Explanation : Sorted by sum, and replaced.

 Sample Input:

2

Gfg 6 7 4

Best 7 6 5

Sample Output

Gfg 17

Best 18

Program:

def sort_dict_by_value_sum(test_dict):
    sorted_dict = {}
    sorted_keys = sorted(test_dict, key=lambda x: sum(test_dict[x]))
    for key in sorted_keys:
        sorted_dict[key] = sum(test_dict[key])
    return sorted_dict

n = int(input().strip())

input_dicts = {}

for _ in range(n):
    data = input().split()
    key = data[0]
    values = list(map(int, data[1:]))
    input_dicts[key] = values

sorted_dicts = sort_dict_by_value_sum(input_dicts)

for key, value in sorted_dicts.items():
    print(key, value)
