3. A strong number is a special number whose sum of factorial of digits is equal to the original number.
For example, 145 is a strong number. Since, 1! + 4! + 5! = 145.
Write a program to find whether the given number is a Strong Number or not.
Input Format:
The input consists of a single integer n.
Output Format:
Output consists of a single word 'Yes' or 'No'.
Sample Input 1:
145
Sample Output 1:
Yes

# strong number
import math

def strong(n):
    if n == 0:
        return 0
    return math.factorial(n % 10) + strong(n // 10)

n = int(input())
c = strong(n)
if c == n:
    print("Yes")
else:
    print("No")

