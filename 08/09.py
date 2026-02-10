def func(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)


a = 34
b = 0
func()
print('---')
func(11, 56, 4, 45, -100, 5.56, 99)
print('---')
func(11, 56, 4, c=a, b=b, a=100, z=-99)
print('---')
func(c=a, b=b, a=100, h=333, k=99, n=-1000)
