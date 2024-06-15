Output is a merged array without duplicates.

Input Format

N1 - no of elements in array 1

Array elements for array 1

N2 - no of elements in array 2

Array elements for array2

Output Format

Display the merged array

Sample Input 1

5

1 

2 

3 

6 

9

4

2 

4 

5 

10

Sample Output 1

1 2 3 4 5 6 9 10

Program:
a=int(input())
l1=[]
d=0
for i in range (0,a):
    b=int(input())
    l1.append(b)
c=int(input())
d=a+c
for i in range(a,d):
    b=int(input())
    l1.append(b)
l1.sort()
l1=set(l1)
l1=list(l1)
d=len(l1)
l1.sort()
for i in range(0,d):
    print(l1[i],end=' ')
