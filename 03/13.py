first_list = [2, 4, 7]
second_list = [3, 5, 7]

c = first_list + second_list
print(c)

# first_list += second_list
# print(first_list)

first_list.extend(second_list)
print(first_list)

c = first_list * 3
print(c)
