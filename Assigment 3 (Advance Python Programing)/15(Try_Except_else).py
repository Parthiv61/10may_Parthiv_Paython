"""When will the else part of try-except-else be executed?"""


#The else part of a try-except-else block in Python is executed only if the try block completes its execution without raising any exceptions. In other words, the code within the else block will run if no exceptions were caught during the execution of the try block.

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
except ValueError:
    print("Invalid input! Please enter valid numbers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("The division result is:", result)
finally:
    print("This block is always executed.")
