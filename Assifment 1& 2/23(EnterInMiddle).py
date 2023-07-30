"""Write a Python function to insert a string in the middle of a string."""

def insert_in_middle(string,middle_string):
    middle_index=len(string)//2
    new_string=string[:middle_index]+middle_string+string[middle_index:]
    print(new_string)

getString=input("Enter a string : ")
getMiddleString=input("Enter a new middle string : ")


insert_in_middle(getString,getMiddleString)