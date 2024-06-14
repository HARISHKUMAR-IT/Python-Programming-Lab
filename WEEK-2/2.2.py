Write a program that returns the last digit of the given number. Last digit is being referred to the least significant digit i.e. the digit in the ones (units) place in the given number.

The last digit should be returned as a positive number.

For example,

if the given number is 197, the last digit is 7

if the given number is -197, the last digit is 7



For example:

Input	Result
197   7
-197  7

Code:

n=int(input())
if n<0:
  n=n*-1
print(n%10)
