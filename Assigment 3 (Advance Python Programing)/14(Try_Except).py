#How many except statements can a try-except block have? Name Some built-in exception classes



#A try-except block in Python can have multiple except statements to handle different types of exceptions. This allows you to handle different exceptional situations in distinct ways.

#her is some try-except examples:

a=int(input("Enter number : "))

try:
    c=10/a
    print("Division = ",c)
except ValueError:
    print("Your Number is invalid!!")