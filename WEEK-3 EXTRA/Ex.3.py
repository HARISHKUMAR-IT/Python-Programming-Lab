3.A toy vendor supplies three types of toys: Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys. The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000. On orders of more than Rs. 100 for key-based toys, a discount of 5% is given, and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500. Assume that the numeric codes 1, 2, and 3 are used for battery based toys, key-based toys, and electrical charging based toys respectively. Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount.


# product code
c = int(input())
n = float(input())
a = n
if (c == 1 and n > 1000):
    a -= (0.10 * n)
elif (c == 2 and n > 100):
    a -= (0.05 * n)
elif (c == 3 and n > 500):
    a -= (0.10 * n)
print(int(a))


