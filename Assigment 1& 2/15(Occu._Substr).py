"""Write a Python program to count occurrences of a substring in a string."""

string=input("Enter string : ")
substr=input("Enter SubString : ")
count=string.count(substr)
print("the number of time",substr,"appears in",string,"is : " ,count)