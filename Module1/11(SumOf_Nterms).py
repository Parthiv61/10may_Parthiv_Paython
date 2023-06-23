"""Write a python program to sum of the first n positive integers."""

n=int(input("Enter positive integers : "))

sum=0

for i in range(1,n+1):
    sum=sum+i 
    print("The sum of first n positive integers is : ",sum)
    