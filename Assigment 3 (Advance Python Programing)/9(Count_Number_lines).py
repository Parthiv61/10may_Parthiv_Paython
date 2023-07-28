"""Write a Python program to count the number of lines in a text file."""

file=open("Session1.txt","w")
file.write("\nWhat are you doing python")
file.close()
file=open("Session1.txt","r")
str=file.readline()
print(str)
a=file.tell()
print(a)
