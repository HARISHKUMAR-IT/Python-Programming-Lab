Write a code to check whether product of digits at even places is divisible by sum of digits

at odd place of a positive integer.

Input Format:

Take an input integer from stdin.

Output Format:

Print TRUE or FALSE.

Example Input:

1256

Output:

TRUE

Example Input:

1595

Output:

FALSE

Code:
def productDigits(n):
    product = 1
    odd_sum = 0
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            product *= digit
        else:
            odd_sum += digit
        n //= 10
    return product % odd_sum == 0


