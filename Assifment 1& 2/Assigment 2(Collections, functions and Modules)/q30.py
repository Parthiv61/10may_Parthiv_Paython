# Write a Python script to sort (ascending and descending) a dictionary by value.

my_dict = {'a': 1, 'c': 3, 'd': 4, 'b': 2}
sorted_ascending = dict(sorted(my_dict.items(), key=lambda item: item[1]))
sorted_descending = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Ascending order:", sorted_ascending)
print("Descending order:", sorted_descending)
