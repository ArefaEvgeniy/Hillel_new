def func(a, b=0, c=-100):
    print("a:", a)
    print("b:", b)
    print("c:", c)


a = 34
b = 0
func(b, 100, a)  # 0, 100, 34
print('---')
func(b, 100)
print('---')
# func()
