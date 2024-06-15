A sentence is a string of single-space separated words where each word consists only of lowercase letters.A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

Example 1:

Input: s1 = "this apple is sweet", s2 = "this apple is sour"

Output: ["sweet","sour"]

Example 2:



Input: s1 = "apple apple", s2 = "banana"

Output: ["banana"]

 Constraints:

1 <= s1.length, s2.length <= 200

s1 and s2 consist of lowercase English letters and spaces.

s1 and s2 do not have leading or trailing spaces.

All the words in s1 and s2 are separated by a single space.

Note:

Use dictionary to solve the problem


Program:
def uncommon_words(s1, s2):
    word_count = {}
    for word in s1.split():
        word_count[word] = word_count.get(word, 0) + 1
    for word in s2.split():
        word_count[word] = word_count.get(word, 0) + 1
    uncommon_words = [word for word, count in word_count.items() if count == 1]
    return ' '.join(uncommon_words)

s1 = input().strip()
s2 = input().strip()

print(uncommon_words(s1, s2))
