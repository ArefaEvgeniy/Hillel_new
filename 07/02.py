my_set = {8, "er", 0, 3.6, (1, 2), 0, True, (99, "c", "RR"), 0, "hello", -100}
my_list = [8, "er", 0, 3.6, (1, 2), 0, True, (99, "c", "RR"), 0, "hello", -100]

print(my_set)
print(my_list)
print(len(my_set))
print(-100 in my_set)
print(-101 in my_set)

print(hash((99, 'c', 'RR')))
print(hash(3.6))
print(hash(0))

input_list = [1, "34", 3.14, "eer", 1, 34, 3.14, "eer", 1, 34, 3.14, "eer", 0, 234,
              "hello", 0, 234, "hello", 0, 234, "hello", 1, "34", 3.14, "eer", 1, 34, 234]

output_list = []
for item in input_list:
    if item not in output_list:
        output_list.append(item)

print(output_list)

output_list_2 = list(set(input_list))
print(output_list_2)
