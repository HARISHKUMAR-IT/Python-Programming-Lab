Given a positive integer N, check whether it can be represented as a product of single digit numbers.

Input Format:

Single Integer input.

Output Format:

Output displays Yes if condition satisfies else prints No.

Example Input: 14

Output: Yes

Example Input:

13

Output: No

Code:

1=list()
n=int(input()) 
c=0 
for i in range(1,n-1): 
    if i>1 and n%i==0:
       1.append(i) 
for i in range(0,len(1)):
   for j in range(0,len(1)): 
      if 1[i]*1[j]==n:
         print("Yes") 
         c=1 
         break
    if c==1: 
       break
if c==0: 
  print("No")
