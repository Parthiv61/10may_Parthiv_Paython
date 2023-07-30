#Write a Python function that takes a list and returns a new list with unique elements of the first list. 
def ul(numbers):
    a = []
    for item in numbers :
        if item not in a:
            a.append(item)
    return a

print(ul([1, 2, 3, 1, 2]))