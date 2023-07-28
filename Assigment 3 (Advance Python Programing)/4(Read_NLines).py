"""Write a Python program to read first n lines of a file. """


file=open("Session1.txt","a")

file.write("how are you python")

file=open("Session1.txt","r")

print(file.readline())