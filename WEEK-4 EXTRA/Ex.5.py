5. A number is stable if each digit occurs the same number of times, i.e., the frequency of each digit in the number is the same. For example, 2277, 4004, 11, 23, 538835, 1010 are examples of stable numbers. Similarly, a number is unstable if the frequency of each digit in the number is NOT the same.
Sample Input:
2277
Sample Output:
Stable Number
Sample Input 2:
121
Sample Output 2:
Unstable Number
For example:
Input
Result
2277
Stable Number



# stable
n = int(input())
s = str(n)
l = len(list(set(s)))
f = list()
for i in set(s):
    f.append(s.count(i))

if f.count(f[0]) == l:
    print("Stable Number")
else:
    print("Unstable Number")
