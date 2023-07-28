"""Write a Python program to append text to a file and display the text. """


file=open("Session1.txt","w")

file.write("Hello python")

file=open("Session1.txt","r")

print(file.read())



