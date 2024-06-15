Given two lists A and B, and B is an anagram of A. B is an anagram of A means B is made by randomizing the order of the elements in A.

We want to find an index mapping P, from A to B. A mapping P[i] = j means the ith element in A appears in B at index j.

These lists A and B may contain duplicates. If there are multiple answers, output any of them.

For example, given

Input

5

12 28 46 32 50

50 12 32 46 28

Output

1 4 3 2 0

Explanation

A = [12, 28, 46, 32, 50]

B = [50, 12, 32, 46, 28]

We should return

[1, 4, 3, 2, 0]

as P[0] = 1 because the 0th element of A appears at B[1], and P[1] = 4 because the 1st element of A appears at B[4], and so on.

Note:

A, B have equal lengths in range [1, 100].
A[i], B[i] are integers in range [0, 10^5].

Program:
def anagram_mappings(A, B):
    # Create a dictionary to map elements of B to their indices
    index_map = {value: index for index, value in enumerate(B)}
    
    # Create the index mapping P using list comprehension
    P = [index_map[element] for element in A]
    
    return P

# Read input
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Find the index mapping P
result = anagram_mappings(A, B)

# Print the result
print(*result)
