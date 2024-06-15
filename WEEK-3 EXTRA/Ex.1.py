1.At a particular company, employees are rated at the end of each year. The rating scale begins at 0.0, with higher values indicating better performance and resulting in larger raises. The value awarded to an employee is either 0.0, 0.4, or 0.6 or more. Values between 0.0 and 0.4, and between 0.4 and 0.6 are never used. The meaning associated with each rating is shown in the following table. The amount of an employee’s raise is $2,400.00 multiplied by their rating.
Rating
Meaning
0.0
Unacceptable Performance
0.4
Acceptable Performance
0.6
Meritorious Performance

Write a program that reads a rating from the user and indicates whether the performance for that rating is unacceptable, acceptable, or meritorious. The amount of the employee’s raise should also be reported. Your program should display an appropriate error message if an invalid rating is entered.
Sample Input 1
0.0
Sample Output 1
Based on that rating, your performance is Unacceptable.
You will receive a raise of $0.00.
Sample Input 2
0.4
Sample Output 2
Based on that rating, your performance is Acceptable.
You will receive a raise of $960.00.
Sample Input 3
0.7
Sample Output 3
Based on that rating, your performance is Meritorious.
You will receive a raise of $1680.00.
Sample Input 4
0.5
Sample Output 4
That wasn’t a valid rating.





#RATING
n=float(input())
if(n>0.0 and n<0.4) or (n>0.4 and n<0.6):
    print("That wasn't a valid rating.")
    r=-1
elif(n==0.0):
    print("Based on that rating, your performance is Unacceptable.")
    r=0
elif(n==0.4):
    r=2400*n
    print("Based on that rating, your performance is Acceptable.")
elif(n==0.6):
    r=2400*n
    print("Based on that rating, your performance is Meritorious.")
if (r!=-1):
    print("You will receive a raise of $%.2f."%r)
