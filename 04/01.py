first_list = [2, 4, 7, 11, 0, 999, 8]
first_list[1:4] = [12]

print(first_list)
print(id(first_list))
second_list = first_list[:]
print(id(second_list))
