#Write a Python program to find the second smallest number in a list.
a = [1,2,3,4,5,6,7,8,9,10,11]
#first 
first_smallno = a[0]
for num in a:
    if num < first_smallno:
        first_smallno = num
#second
second_smallno = None
for num in a:
    if num != first_smallno:
        if second_smallno is None or num < second_smallno:
            second_smallno = num
print("Second first_smallno number:", second_smallno)
