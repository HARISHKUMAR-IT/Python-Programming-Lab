4. Rakesh loves playing with numbers. He took the Fibonacci series and wants to find the sum of squares of the series until a given value. Write a code that implements his task.
Input Format:
Single Integer N
Output Format:
Display the sum of squares of the Fibonacci series until the Nth term.
Example Input:
9
Output:
1870
Explanation:
The numbers are: 1 1 2 3 5 8 13 21 34
Sum of their squares is: 1 + 1 + 4 + 9 + 25 + 64 + 169 + 441 + 1156 = 1870
For example:
Input
Result
9
1870



# fibonacci
def fiba(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fiba(n - 1) + fiba(n - 2)

n = int(input())
d = 0

for i in range(1, n + 2):
         c = fiba(i)
          d = d + (c * c)
    print(d)
