"""Write a Python program to get the Factorial number of given number."""


num=int(input("Enter number:"))

Factorial=1

if num==0:
    print("The Factorial for 0 is 1")

elif num<=0:
    print("Sorry, factorial does not exist for negative numbers")

else:
    for i in range(1,num+1):
     Factorial=Factorial*i
    print("The Factorial for", num, "is", Factorial) 

