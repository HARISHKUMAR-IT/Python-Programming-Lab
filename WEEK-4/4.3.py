A Number is said to be Disarium number when the sum of its digit raised to the power of their respective positions becomes equal to the number itself. Write a program to print number is Disarium or not.

Input Format:

Single Integer Input from stdin.

Output Format:

Yes or No.

Example Input:

175

Output: Yes

Explanation 1^1+7^2+5^3 = 175

Example Input: 123

Output:

No

For example:

Input Result

175   Yes
123   No

Code:

n=int(input()) s=len(str(n))
t=n
p=0
while t!=0: 
  d=t%10 
  p=p+(d**s) 
  s=s-1 
  t=t//10
if p==n:
  print("Yes")
else: 
  print("No")
