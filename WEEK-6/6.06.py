Given an array A of sorted integers and another non negative integer k, find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.

Input Format

1.      First line is number of test cases T. Following T lines contain:

2.      N, followed by N integers of the array

3.      The non-negative integer k

Output format

Print 1 if such a pair exists and 0 if it doesn’t.

Example

Input

1

3 

1 

3 

5

4

Output:

1

Input

1

3 

1 

3 

5

99

Output

0

  Program :

  a=int(input())

for  i in range(a):
    l=[]
    b=int(input())
    t=1
    for j in range(b):
        l.append(int(input()))
    
    c=int(input())
    for m in range(len(l)-1):
        
        for s in range(m+1,len(l)):
        
            if (abs(l[m]-l[s])==c ):
                
                t=0
            
                break
        
    if(t==1):
        print("0")
    else:
        print("1")
        
