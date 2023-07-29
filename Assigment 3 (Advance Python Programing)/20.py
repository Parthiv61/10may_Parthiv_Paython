"""Write python program that user to enter only odd numbers, else will 
raise an exception. """

number=int(input("Enter Your Number : "))

try:
    number % 2 != 0
    print("This number is valid number")
except:
    print("Please Enter valid number")

