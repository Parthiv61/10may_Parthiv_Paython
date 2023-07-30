# Write a Python program to replace last value of tuples in a list.
a = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
for i in range(len(a)):
    upd_list = list(a[i])
    upd_list[-1] = 100
    a[i] = tuple(upd_list)
print(a)
