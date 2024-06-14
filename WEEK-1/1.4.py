Alfred buys an old scooter for Rs. X and spends Rs. Y on its repairs. If he sells the scooter for Rs. Z (Z>X+Y). Write a program to help Alfred to find his gain percent. Get all the above-mentioned values through the keyboard and find the gain percent.

Input Format:

The first line contains the Rs X
The second line contains Rs Y
The third line contains Rs Z

Sample Input:
  
10000
250
15000

Sample Output:

46.34 is the gain percent.


For example:

Input	Result
45500 30.43 is the gain percent
500
60000

Code:

a=int(input())
b=int(input())
c=int(input())
d=c-(a+b)
e=(d/(a+b))*100
print('%0.2f'%abs(e),"is the gain percent.")
