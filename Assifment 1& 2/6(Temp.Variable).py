"""Write python program that swap two number with temp variable and without temp variable."""


"""Swap using temp. variable"""
x=4
y=6

#creat one temp. variable 
temp=x
x=y
y=temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))


"""Swap using without temp. variable"""
x=13
y=16

x,y=y,x
print("The value of x after swapping:",x)
print("The value of y after swapping:",y)