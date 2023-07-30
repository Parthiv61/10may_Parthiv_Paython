"""Write a Python function to reverses a string if its length is a multiple of 4."""

def reverses_string(string):
    if len(string)%4==0:    
       print(string[::-1])
    
    else:
        print(string)


getstring=input("Enter a string : ")
reverses_string(getstring)