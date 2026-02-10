def func(a, v, d, r):
    print("a:", a)
    print("v:", v)
    print("d:", d)
    print("r:", r)


func(v=100, a=333, r=99, d=1000)
print('---')
my_dict_1 = {"v": -100, "a": 5.56, "r": 99, "d": 1000}
func(**my_dict_1)  # func(v=-100, a=5.56, r=99, d=1000)
