#Write a Python program to find the highest 3 values in a dictionary  
# Sample dictionary
my_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6
}

# Method 1: Using sorted() function with a lambda function
highest_values = sorted(my_dict.values(), reverse=True)[:3]
print("Highest 3 values using sorted():", highest_values)

