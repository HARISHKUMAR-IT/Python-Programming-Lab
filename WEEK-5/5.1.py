Two string values S1, S2 are passed as the input. The program must print first N characters present in S1 which are also present in S2.

Input Format:

The first line contains S1.
The second line contains S2.
The third line contains N.

Output Format:

The first line contains the N characters present in S1 which are also present in S2.

Boundary Conditions:

2 <= N <= 10
2 <= Length of S1, S2 <= 1000

Example Input/Output 1:

Input:

abcbde
cdefghbb
3

Output:

bcd

Note:

b occurs twice in common but must be printed only once.
 Program:
  def find_common_characters(S1, S2, N):
    # Convert S2 into a set for faster membership testing
    set_S2 = set(S2)
    # To keep track of added characters and maintain order from S1
    common_chars = []
    
    added_chars = set()
   
    
    for char in S1:
        if char in set_S2 and char not in added_chars:
            common_chars.append(char)
            added_chars.add(char)
            
            if len(common_chars) == N:
                break
   
    return ''.join(common_chars)


import sys
input = sys.stdin.read
data = input().split()
S1 = data[0]
S2 = data[1]
N = int(data[2])

print(find_common_characters(S1, S2, N))
