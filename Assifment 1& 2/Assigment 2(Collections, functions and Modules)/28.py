# Write a Python function to get the largest number, smallest num and sum of all from a list1
def list_stats(numbers):
    if not numbers:
        return None, None, 0  
    
    largest = max(numbers)
    small = min(numbers)
    total = sum(numbers)

    return largest, small, total

# Example usage:
my_list = [1,3,5,7,9]
largest, small, sum = list_stats(my_list)

print("Largest number:", largest)
print("Smallest number:", small)
print("Sum of all numbers:", sum)
