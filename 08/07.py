def func(a, b=-1, *args):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    # for item in args:
    #     print("item:", item)


a = 34
b = 0
func(b, 100, a)  # 0, 100, 34
print('---')
func(b, 100, a, 1000)
print('---')
func(b, 100, a, 1000, 10000, -100, 5.56, 99)
print('---')
func(b, 100)
print('---')
func(b)
# print('---')
# func(11)
# print('---')
# func()
