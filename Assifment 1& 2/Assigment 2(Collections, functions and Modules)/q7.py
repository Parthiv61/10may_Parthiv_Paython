#Write a Python program to remove duplicates from a list.  
list_a = [1,2,5,6,1,2,5]
print ("The original list is : "
        + str(list_a))
 
list_a = list(set(list_a))

print ("The list after removing duplicates : "
        + str(list_a))