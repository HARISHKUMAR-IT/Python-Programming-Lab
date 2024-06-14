Write a program to convert strings to an integer and float and display its type.

Sample Input:

10
10.9

Sample Output:

10,<class 'int'>
10.9,<class 'float'>

For example:

Input	Result
10    10,<class 'int'>
10.9  10.9,<class 'float'>


a=int(input())
b=float(input())
c=type(a)
d=type(b)
print(a,c,sep=",")
print('%0.1f'%abs(b),d,sep=",")
