#Write a Python program to map two lists into a dictionary  
keys = ['key1', 'key2', 'key3', 'key4']
values = ['value1', 'value2', 'value3', 'value4']
mapped_dict_new = dict(zip(keys, values))
print("Mapped dictionary using the dict() constructor:", mapped_dict_new)
