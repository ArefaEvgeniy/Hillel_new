my_list = [10, 20, 30, 40, -10, 50, 60, 0, 70, 80, 44, 90, 100, -50]

new_list = []
for item in my_list:
    if item >= 0:
        if item < 50:
            new_list.append(item ** 2)
        else:
            new_list.append(item * 2)
print(new_list)

new_list_2 = [item ** 2 if item < 50 else item * 2 for item in my_list
              if item >= 0]
print(new_list_2)
