Problem Description:

Develop a Python program that safely calculates the square root of a number provided by the user. Handle exceptions for negative inputs and non-numeric inputs.

Input Format:

User inputs a number.

Output Format:

Print the square root of the number or an error message if an exception occurs.

Code:

#Square root exceptions
try:
    n=input()
    if '.' in n:
        n=float(n)
    else:
        n=int(n)
    if n>=0 and '.' not in str(n):
        print("The square root of %.1f"%n,"is %.2f"%(n**0.5))
        #print("The square root of",n,"is",round((n**0.5),2))
    elif '.' in str(n):
        print("The square root of",n,"is",round((n**0.5),2))
    elif n<0:
        raise Exception
except ValueError:
    print("Error: could not convert string to float")
except:
    print("Error: Cannot calculate the square root of a negative number.")
