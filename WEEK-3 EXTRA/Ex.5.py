5. Write a Python program to calculate profit and loss (Cost Price and Selling Price is given as inputs).
Sample Test Cases
Test Case 1
Input 6000.00 6700.50
Output Profit amount: Rs. 700.50
Test Case 2
Input 600.50 520.00
Output Loss amount: Rs. 80.50

# profit or loss
cp = float(input())
sp = float(input())
if sp > cp:
    pl = sp - cp
    print("Profit amount: Rs. %.2f" % pl)
elif cp > sp:
    pl = cp - sp
    print("Loss amount: Rs. %.2f" % pl)
else:
    print("No profit No loss")
