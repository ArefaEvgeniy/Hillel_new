import copy


first_list = [2, 4, 7, [1, 2, 3], 11, 11.333]

new_list = copy.deepcopy(first_list)

new_list[3].append(4)

print(first_list)
print(new_list)
