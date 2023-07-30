#Write a Python program to remove an empty tuple(s) from a list of tuples.
def removet(li):
    li=[ num for num in li if num]
    return li
li=[ (), ('a', '1', '2'), (), ('3', '4', '5', '6') ]
print(removet(li))
