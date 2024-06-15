Given an listof integers, sort the array in ascending order using the Bubble Sort algorithm above. Once sorted, print the following three lines:

1.      List is sorted in numSwaps swaps., where numSwaps is the number of swaps that took place.

2.      First Element: firstElement, the  first element in the sorted list.

3.      Last Element: lastElement, the last element in the sorted list.

For example, given a worst-case but small array to sort: a=[6,4,1]. It took  3 swaps to sort the array. Output would be

Array is sorted in 3 swaps.  
First Element: 1  
Last Element: 6   
Input Format

The first line contains an integer,n , the size of the list a .
The second line contains  n,  space-separated integers a[i].

Constraints

·         2<=n<=600

·         1<=a[i]<=2x106.

Output Format

You must print the following three lines of output:

1.      List is sorted in numSwaps swaps., where numSwaps is the number of swaps that took place.

2.      First Element: firstElement, the  first element in the sorted list.

3.      Last Element: lastElement, the last element in the sorted list.

Sample Input 0

3

1 2 3

Sample Output 0

List is sorted in 0 swaps.

First Element: 1

Last Element: 3

Code:
def bubble_sort(arr):
    n = len(arr)
    num_swaps = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                num_swaps += 1
    
    print("List is sorted in {} swaps.".format(num_swaps))
    print("First Element:", arr[0])
    print("Last Element:", arr[-1])

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    bubble_sort(arr)

main()
