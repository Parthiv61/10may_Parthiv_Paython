"""Write a Python program to add 'ing' at the end of a given string (length 
should be at least 3). If the given string already ends with 'ing' then add 
'ly' instead if the string length of the given string is less than 3, leave it 
unchanged."""

string=input("Enter a string : ")

length=len(string)

if length<3:
    New_string = string

elif string[-3:]=="ing":
    New_string = string + "ly" 

else:
    New_string = string + "ing"


print("New string = ",New_string )


