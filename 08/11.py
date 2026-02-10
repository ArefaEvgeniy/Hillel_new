def func(a, v, d, r=0):
    print("a:", a)
    print("v:", v)
    print("d:", d)
    print("r:", r)


func(100, 333, 99, 1000)
my_list_1 = [-100, 5.56, 99]
my_list_2 = [-100, 5.56, 99, 1000]
my_list_3 = [-100, 5.56, 99, 1000, 666, 456]
print('---')
func(*my_list_1)  # func(my_list[0], my_list[1], my_list[2])
print('---')
func(*my_list_2)  # func(my_list[0], my_list[1], my_list[2], my_list[3])
print('---')
func(*my_list_3[:4])  # func(my_list[0], my_list[1], my_list[2], my_list[3])
