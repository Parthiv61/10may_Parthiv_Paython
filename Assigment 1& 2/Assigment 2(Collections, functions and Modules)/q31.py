#Write a Python script to concatenate following dictionaries to create a new one.
d_1 = {'A': 15, 'B': 10, 'C' : 12 }  
d_2 = {'E': 18,'B': 20,'D' : 16 }  
d_1.update(d_2)  
print('Updated dictionary:')  
print(d_1)  