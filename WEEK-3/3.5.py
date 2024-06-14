Write a program to calculate and print the Electricity bill where the unit consumed by the user is given from test case. It prints the total amount the customer has to pay. The charge are as follows: 

Unit                                Charge / Unit

Upto 199                               @1.20

200 and above but less than 400        @1.50

400 and above but less than 600        @1.80

600 and above                          @2.00

If bill exceeds Rs.400 then a surcharge of 15% will be charged and the minimum bill should be of Rs.100/- 

Sample Test Cases

Test Case 1 

Input

50 

Output

100.00 

Test Case 2

Input 

300

Output 

517.50



For example:

Input 	Result
100.00  120.00

Code:

n=float(input())
if n<=199:
    a=n*1.20
elif n>=200 and n<400:
    a=n*1.50
elif n>=400 and n<600:
    a=n*1.80
elif n>=600:
    a=n*2.00
    
if (a<100):
    a=100
elif a>400:
    a=a+(0.15*a)
print("%.2f"%a)
