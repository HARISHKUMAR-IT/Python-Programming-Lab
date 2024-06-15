Given a tuple and a positive integer k, the task is to find the count of distinct pairs in the tuple whose sum is equal to K.

Examples:

Input: t = (5, 6, 5, 7, 7, 8 ), K = 13 
Output: 2 
Explanation: 
Pairs with sum K( = 13) are  {(5, 8), (6, 7), (6, 7)}. 
Therefore, distinct pairs with sum K( = 13) are { (5, 8), (6, 7) }. 
Therefore, the required output is 2.

  Program:
def count_distinct_pairs(t, K):
    pair_set = set()
    seen = set()
    count = 0
    
    for num in t:
        complement = K - num
        if complement in seen and (complement, num) not in pair_set and (num, complement) not in pair_set:
            pair_set.add((complement, num))
            count += 1
        seen.add(num)
    
    return count

t = tuple(int(x) for x in input().split(','))
K = int(input())

print(count_distinct_pairs(t, K))
