Write a program to eliminate the common elements in the given 2 arrays and print only the non-repeating

elements and the total number of such non-repeating elements.

Input Format:

The first line contains space-separated values, denoting the size of the two arrays in integer format respectively.

The next two lines contain the space-separated integer arrays to be compared.

Sample Input:

5 4

1 2 8 6 5

2 6 8 10

Sample Output:

1 5 10

3

Sample  Input: 

5 5

1 2 3 4 5

1 2 3 4 5

Sample Output:

NO SUCH ELEMENTS


Program:
n, m = input().split()
n = int(n)
m = int(m)
arr1 = [int(x) for x in input().split()]
arr2 = [int(x) for x in input().split()]

non_repeating_elements = set(arr1).symmetric_difference(set(arr2))

if non_repeating_elements:
    print(*non_repeating_elements)
    print(len(non_repeating_elements))
else:
    print("NO SUCH ELEMENTS")
