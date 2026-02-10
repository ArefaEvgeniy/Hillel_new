def func(a, g, *args, b, c, **kwargs):
    print("a:", a)
    print("g:", g)
    print("b:", b)
    print("c:", c)
    print("args:", args)
    print("kwargs:", kwargs)


a = 34
b = 0
func(11, 56, 4, c=a, b=b, r=100, z=-99)
print('---')
func(100, 5, c=a, b=b, h=333, k={1: 12, '4': 55, 'a': 667}, n=[-1000, 44, 3434, 234])
