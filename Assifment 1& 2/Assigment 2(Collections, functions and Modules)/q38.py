#Write a Python program to print all unique values in a dictionary. 
a = [{"a":"1"}, {"V": "2"}, {"c": "1"}, {"a": "1"}]
print("Original List: ",a)
u_value = set( val for dic in a for val in dic.values())
print("Unique Values: ",u_value)
