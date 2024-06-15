A number is considered to be ugly if its only prime factors are 2, 3 or 5.

[1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, …] is the sequence of ugly numbers.

Task:

complete the function which takes a number n as input and checks if it's an ugly number.

return ugly if it is ugly, else return not ugly

Hint:

An ugly number U can be expressed as: U = 2^a * 3^b * 5^c, where a, b and c are nonnegative integers.

  Code:
def checkUgly(n):
    if n <= 0:
        return "not ugly"
    
    for p in [2, 3, 5]:
        while n % p == 0:
            n //= p
    
    return "ugly" if n == 1 else "not ugly"
