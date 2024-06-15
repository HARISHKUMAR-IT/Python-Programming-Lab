Write a Python program that performs division and modulo operations on two numbers provided by the user. Handle division by zero and non-numeric inputs.

Input Format:

Two lines of input, each containing a number.

Output Format:

Print the result of division and modulo operation, or an error message if an exception occurs.

For example:

Input	Result
10
2
Division result: 5.0
Modulo result: 0
7
3
Division result: 2.3333333333333335
Modulo result: 1
8
0
Error: Cannot divide or modulo by zero.

program:

try:
    a=float(input())
    b=float(input())
    c=a/b
except ValueError:
    print("Error: Non-numeric input provided.")
except ZeroDivisionError:
    print("Error: Cannot divide or modulo by zero.")
else:
    print("Division result:",a/b)
    print("Modulo result:",int(a%b))
