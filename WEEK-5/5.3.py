Consider the below words as key words and check the given input is key word or not.

keywords: {break, case, continue, default, defer, else, for, func, goto, if, map, range, return, struct, type, var}

Input format:

Take string as an input from stdin.

Output format:

Print the word is key word or not.

Example Input:

break

Output:

break is a keyword

Example Input:

IF

Output:

IF is not a keyword

Program:
n=input()
if (n=='break'or n=='case' or n=='continue' or n=='default' or n=='defer' or n=='else' or n=='for' or n=='func' or n=='goto' or n=='if' or n=='map' or n=='range' or n=='return' or n=='struct' or n=='type' or n=='var'):
    print(n,"is a keyword")
else:
    print(n,"is not a keyword") 
