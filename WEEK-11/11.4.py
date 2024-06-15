Problem Description:

Write a Python program that asks the user for their age and prints a message based on the age. Ensure that the program handles cases where the input is not a valid integer.



Input Format:

A single line input representing the user's age.



Output Format:

Print a message based on the age or an error if the input is invalid.

For example:

Input	Result
25
You are 25 years old.
rec
Error: Please enter a valid age.
-5
Error: Please enter a valid ageWrite a Python program that asks the user for their age and prints a message based on the age. Ensure that the program handles cases where the input is not a valid integer.

Input Format: A single line input representing the user's age.

Output Format: Print a message based on the age or an error if the input is invalid.


For example:

Input	Result
twenty
Error: Please enter a valid age.
25
You are 25 years old.
-1
Error: Please enter a valid age.

Code:
#Age exception
try:
    n=int(input())
    if n>=0:
        print("You are %d years old."%n)
    else:
        raise Exception
except:
    print("Error: Please enter a valid age.")
