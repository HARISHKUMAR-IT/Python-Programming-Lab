1. Write a program to check whether a given number is a perfect number or not.
A perfect number is a positive number which sum of all positive divisors excluding that number is equal to that number.
For example, 6 is a perfect number since the divisors of 6 are 1, 2, and 3. Sum of its divisors is 1 + 2 + 3 = 6.
Sample Test Cases
Test Case 1
Input
6
Output
YES
Test Case 2
Input
45
Output
NO

# perfect number
n = int(input())
c = 0
for i in range(1, (n // 2) + 1):
    if n % i == 0:
        c += i
if c == n:
    print("YES")
else:
    print("NO")
