def func(a, b=1, c=-1, **kwargs):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("kwargs:", kwargs)


a = 34
b = 0
func(c=a, b=b, a=100)
print('---')
func(c=a, b=b, a=100, z=-99)
print('---')
func(c=a, b=b, a=100, h=333, k=99, n=-1000)
print('---')
func(a, b, 100, z=333, t=99, v=1000)
func(a=100, z=333, t=99, c=1000)
