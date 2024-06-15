Write a python program to count all letters, digits, and special symbols respectively from a given string


For example:

Input	Result
rec@123
3
3
1

Program:

s=input()
l=d=c=0

for i in s:
    if i.isalpha()==True:
        l=l+1
    elif i.isdigit()==True:
        d=d+1
    else:
        c=c+1
print(l)
print(d)
print(c)
