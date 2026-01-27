import copy


first_list = [2, 4, 7, 11, 11.333, 0, 999, 8, -11]
second_list = first_list.copy()
third_list = first_list[:]
new_list = copy.copy(first_list)

second_list.append(55)
third_list.remove(0)
new_list.sort()

print(first_list)
print(second_list)
print(third_list)
print(new_list)
