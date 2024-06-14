Write a program to find the count of non- repeated digits in a given number N. The number will be passed to the program as an input of type int.

Assumption: The input number will be a positive integer number >= 1 and <= 25000.

Some examples are as below.

If the given number is 292, the program should return 1 because there is only 1 non-repeated digit '9' in this number

If the given number is 1015, the program should return 2 because there are 2 non- repeated digits in this number, '0', and '5'.

If the given number is 108, the program should return 3 because there are 3 non-- repeated digits in this number, '1', '0', and '8'.

If the given number is 22, the function should return 0 because there are NO non-- repeated digits in this number.

For example:

Input Result

292   1
1015  2
108   3
22    0

Code:

n=int(input())
s=str(n) 
1=list(set(s))
d=0
for i in range(0,len(1)):
  c=0 
  for j in range(0,len(s)):
    if int(1[i])==int(s[j]): 
      c=c+1  
      if c==1: 
        d=d+1
print(d)
