Find the intersection of two sorted arrays.

OR in other words,

Given 2 sorted arrays, find all the elements which occur in both the arrays.

Input Format

The first line contains T, the number of test cases. Following T lines contain:

1.      Line 1 contains N1, followed by N1 integers of the first array

2.      Line 2 contains N2, followed by N2 integers of the second array

Output Format

The intersection of the arrays in a single line

Example

Input:

1

3 10 17 57

6 2 7 10 15 57 246

Output:

10 57

Input:

1

7 

1 

2 

3 

3 

4 

5 

6

2 

1 

6

Output:

1 6

Program :
T=int(input())
while(T):
    L1=[]
    L2=[]
    n1=int(input())
    while(n1):
        L1.append(int(input()))
        n1-=1
    n2=int(input())
    while(n2):
        L2.append(int(input()))
        n2-=1
    L3=[]
    for x in L1:
        if x in L2:
            L3.append(x)
    L4=' '.join(str(e) for e in L3)
    print(L4)
    T=T-1
