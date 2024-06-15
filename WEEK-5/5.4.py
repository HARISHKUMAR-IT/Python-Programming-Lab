Given two Strings s1 and s2, remove all the characters from s1 which is present in s2.

 

Constraints

 

1<= string length <= 200

 

Sample Input 1

 

experience

enc

 

Sample Output 1

 

xpri

Program:
s1=input()
s2=input()
s=''
for i in range(0,len(s1)):
    if s1[i] not in s2:
        s=s+s1[i]
print(s)
