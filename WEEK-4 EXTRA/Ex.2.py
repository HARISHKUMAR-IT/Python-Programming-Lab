2. Write a program that reads a positive integer, n, from the user and then displays the sum of all of the integers from 1 to n.
Sample Input
10
Sample Output
The sum of the first 10 positive integers is 55.0
For example:
Input
Result
10
The sum of the first 10 positive integers is 55.0


# sum
def sum(n):
    if n == 1:
        return 1
    return n + sum(n - 1)

n = int(input())
c = sum(n)
print("The sum of the first ", n, " positive integers is ", c, '.0', sep='')
