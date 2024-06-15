There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.

Given a string text of words separated by a single space (no leading or trailing spaces) and a string brokenLetters of all distinct letter keys that are broken, return the number of words in text you can fully type using this keyboard.

Example 1:

Input: text = "hello world", brokenLetters = "ad"

Output: 

1

Explanation: We cannot type "world" because the 'd' key is broken.

Program :
a=input()
a=a.split(" ")


b=input()
count=0


for i in range(len(a)):
 if a[i].find(b):
  count+=1
if count>len(b):
 print(len(b))
else:
 print(count-1)

    
