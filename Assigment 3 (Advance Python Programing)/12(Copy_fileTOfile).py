"""Write a Python program to copy the contents of a file to another file."""


file=open("source.txt","w")
file.write("Hello friends, this is python!!!")
file=open("destination.txt","x")


file=open("source.txt","r")
content=file.read()
file.close()

with open("destination.txt","a") as file:
    file.write(content)

print("File copied sucessfully")

