Determine the factors of a number (i.e., all positive integer values that evenly divide into a number).

For example:

Input Result

20    1 2 4 5 10 20

Code:

n=int(input()) 
1=list() 
for i in range(1,n+1):
  if n%i==0:
    1.append(i) 
for i in range(0,len(1)): 
  print(l[i],end=' ')
