To find the frequency of numbers in a list and display in sorted order.

Constraints: 

1<=n, arr[i]<=100 

Input: 

1 68 79 4 90 68 1 4 5 

output:

 1 2

 4 2

 5 1

 68 2

 79 1 

90 1

Code:
#frequency
s=input()
z=s.split()
z=[int(z[i]) for i in range(0,len(z))]
z.sort()
l=list()

for i in range(0,len(z)):
    c=1
    for j in range(i+1,len(z)):
        if z[i]==z[j]:
            c=c+1
    if z[i] not in l:
        print(z[i],c,end=' ')
        l.append(z[i])
        print()
   
   
