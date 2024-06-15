Find if a String2 is substring of String1. If it is, return the index of the first occurrence. else return -1.

Sample Input 1 

thistest123string

123

Sample Output 1 

8

Code:
def find_substring(String1, String2):
    return String1.find(String2)

String1 = "thistest123string"
String2 = "123"
print(find_substring(String1, String2))  # Output: 8
