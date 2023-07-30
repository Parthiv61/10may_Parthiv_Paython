#Write a Python program to check whether a list contains a sub list 
main_list = [1, 2, [3, 4, 5] ,6, 7, 8, 9, 10]
sub_list = [3, 4, 5]

if sub_list in main_list:
    print("main_list contains sub_list.")
else:
    print("main_list does not contain sub_list.")


