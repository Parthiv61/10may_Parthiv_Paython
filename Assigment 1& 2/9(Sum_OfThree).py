"""Write a Python program to sum of three given integers. However, if two values are equal sum will be zero."""

def SumOfThree(a,b,c):
    if a==b or b==c or c==a:
        print("sum is 0")
    else:
        print("sum : ",a+b+c)
    
GetA=int(input("Enter value of A : " ))
GetB=int(input("Enter value of B : " ))
GetC=int(input("Enter value of C : " ))


SumOfThree(GetA,GetB,GetC)