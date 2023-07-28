"""How Do You Handle Exceptions With Try/Except/Finally In Python? 
Explain with coding snippets."""


a=int(input("Enter Value of A : "))
b=int(input("Enter Value of B : "))

try:
    c=a/b
except ValueError:
    print("Invalid input!!!")
except ZeroDivisionError:
    print("Can not divided by zero")
else:
    print("your division is : ",c)
finally:
    print("this block excute automatically even after error")
