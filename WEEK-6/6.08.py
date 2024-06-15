Write a Python program to Zip two given lists of lists.

Input:

m : row size

n: column size

list1 and list 2 :  Two lists

Output

Zipped List : List which combined both list1 and list2

Sample test case

Sample input

2

2
1 

3

5

7
2

4

6

8
Sample Output

[[1, 3, 2, 4], [5, 7, 6, 8]]

Program :
a=int(input())
b=int(input())
L=[]
for i in range(a):
    k=[]
    for i in range(b):
        
        p=int(input())
        k.append(p)
    L.append(k)
T=[]
for i in range(a):
    k=[]
    for i in range(b):
        
        p=int(input())
        k.append(p)
    T.append(k)
g=[]
for i in range(len(T)):
    g.append(L[i]+T[i])
print(g)
