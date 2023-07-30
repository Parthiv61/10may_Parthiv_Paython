#Write a Python program to convert a list of tuples into a dictionary.

my_list = [('a', 1), ('b', 2), ('c', 3)]
my_dict = {key: value for key, value in my_list}
print("Dictionary:", my_dict)
