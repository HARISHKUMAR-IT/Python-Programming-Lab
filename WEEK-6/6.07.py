Write a program to print all the locations at which a particular element (taken as input) is found in a list and also print the total number of times it occurs in the list. The location starts from 1.

 

For example, if there are 4 elements in the array:

 

5

6

5

7

 

If the element to search is 5 then the output will be:

 

5 is present at location 1

5 is present at location 3

5 is present 2 times in the array.

 

Sample Test Cases

 

Test Case 1

 

Input

 

4

5

6

5

7

5

 

Output

 

5 is present at location 1.

5 is present at location 3.

5 is present 2 times in the array.

 

Test Case 2

 

Input

 

5

67

80

45

97

100

50

 

Output

 

50 is not present in the array.

Program :
n = int(input())
arr = [int(input()) for _ in range(n)]
target = int(input())


locations = [i+1 for i, num in enumerate(arr) if num == target]
count = len(locations)


if count == 0:
    print(f"{target} is not present in the array.")
else:
    for loc in locations:
        print(f"{target} is present at location {loc}.")
    print(f"{target} is present {count} times in the array.")
