Problem Description:

Write a Python script that asks the user to enter a number within a specified range (e.g., 1 to 100). Handle exceptions for invalid inputs and out-of-range numbers.

Input Format:

User inputs a number.

Output Format:

Confirm the input or print an error message if it's invalid or out of range.

For example:

Input	Result
1
Valid input.
101
Error: Number out of allowed range
rec
Error: invalid literal for int()

Code:
                      #Exception

try:
    n=int(input())
    if n>=1 and n<=100:
        print("Valid input.")
    else:
        raise Exception
except ValueError:
    print("Error: invalid literal for int()")
except:
    print("Error: Number out of allowed range")

    
