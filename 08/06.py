def func(b, a=1, c=-1):
    print("a:", a)
    print("b:", b)
    print("c:", c)


a = 34
b = 0
func(c=a, b=b, a=100)
print('---')
func(b=b, a=100)
print('---')
func(b=b, c=100)
