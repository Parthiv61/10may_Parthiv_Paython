#Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
def newstring(ab):
  a = 0

  for word in ab:
    if len(word) > 1 and word[0] == word[-1]:
      a += 1
  return a

print(newstring(['aba','cdc','ads']))
