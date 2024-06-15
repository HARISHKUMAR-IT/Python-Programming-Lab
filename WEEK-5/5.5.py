Write a python to read a sentence and print its longest word and its length


For example:

Input	Result
This is a sample text to test
sample
6
Program:
n=input()
p=n.split()

a=max(p,key=len)
print(a)
x=len(a)
print(x)
