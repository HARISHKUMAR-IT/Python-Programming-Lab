Robert  is having 2 strings consist of uppercase & lowercase english letters. Now he want to compare those two strings lexicographically. The letters' case does not matter, that is an uppercase letter is considered equivalent to the corresponding lowercase letter.


Input
The first line contains T. Then T test cases follow.

Each test case contains a two lines contains a string. The strings' lengths range from 1 to 100 inclusive. It is guaranteed that the strings are of the same length and also consist of uppercase and lowercase Latin letters.

Output
If the first string is less than the second one, print "-1".
If the second string is less than the first one, print "1".
If the strings are equal, print "0".
Note that the letters' case is not taken into consideration when the strings are compared.

Constraints
                      1≤T≤50
                      String length≤100

Code:
def compare_strings_lexicographically(T, test_cases):
    results = []
    for case in test_cases:
        str1, str2 = case
        str1_lower = str1.lower()
        str2_lower = str2.lower()
        if str1_lower < str2_lower:
            results.append("-1")
        elif str1_lower > str2_lower:
            results.append("1")
        else:
            results.append("0")
    return results

if __name__ == "__main__":
    T = int(input().strip())
    test_cases = [(input().strip(), input().strip()) for _ in range(T)]
    results = compare_strings_lexicographically(T, test_cases)
    for result in results:
        print(result)
