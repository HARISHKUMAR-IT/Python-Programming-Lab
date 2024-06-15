4. Write a program that accepts 5 inputs and returns the count of how many of those 5 are even.
For example, If the five inputs are 12, 17, 19, 14, and 115, there are two even numbers 12 and 14. So, the program must return 2.
Similarly, If the five inputs are 15, 0, -12, 19, and 28, there are three even numbers 0, -12, and 28. So, the program must return 3.
Observe that zero is also considered an even number.
For example:
Input
Result
12 17 19 14 115
2
15 0 -12 19 28
3



# even count
n = 5
c = 0
for i in range(0, n):
    a = int(input())
    if a % 2 == 0:
        c = c + 1
print(c)


