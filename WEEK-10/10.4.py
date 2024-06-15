An list contains N numbers and you want to determine whether two of the numbers sum to a given number K. For example, if the input is 8, 4, 1, 6 and K is 10, the answer is yes (4 and 6). A number may be used twice.

Input Format

The first line contains a single integer n , the length of list

The second line contains n space-separated integers, list[i].

The third line contains integer k.

Output Format

Print Yes or No.

Sample Input

7

0 1 2 4 6 5 3 

1 

Sample Output

Yes

Code:
def two_sum(nums, target):
    num_set = set()
    for num in nums:
        complement = target - num
        if complement in num_set:
            return "Yes"
        num_set.add(num)
    return "No"

n = int(input())
nums = list(map(int, input().split()))
k = int(input())
print(two_sum(nums, k))
