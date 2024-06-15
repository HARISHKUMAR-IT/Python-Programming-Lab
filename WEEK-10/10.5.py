Write a Python program for binary search.

For example:

Input	         Result
1,2,3,5,8,6    False
3,5,9,45,42,42 True

program:
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2  # Calculate the mid index

        if arr[mid] < x:
            low = mid + 1  # Ignore the left half
        elif arr[mid] > x:
            high = mid - 1  # Ignore the right half
        else:
            return mid  # x is present at mid

    return -1  # x is not present in array

# Read input from user
arr = input()
x = int(input())

# Process input
arr = arr.split(',')
arr = [int(element) for element in arr]
arr.sort()

# Function call
result = binary_search(arr, x)

# Output result
if result != -1:
    print("True")
else:
    print("False")
