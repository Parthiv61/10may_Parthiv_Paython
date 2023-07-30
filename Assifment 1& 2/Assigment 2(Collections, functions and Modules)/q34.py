#Write a Python program to check multiple keys exists in a dictionary  

my_dictionary = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3',
    'key4': 'value4',
    'key5': 'value5'
}


keys_to_check = ['key2', 'key4', 'key6']
print("Method 4:")
results = [(key, "exists" if key in my_dictionary else "does not exist") for key in keys_to_check]

for key, status in results:
    print(f"'{key}' {status} in the dictionary.")
