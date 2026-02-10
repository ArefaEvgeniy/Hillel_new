name = "Bob"


def func_1():
    name = "Alice"
    print(f"Hello, {name}!")
    return name


def func_2():
    def func_3():
        print(f"Hi, {name}!")

    name = "Charlie"
    func_3()
    print(f"Goodbye, {name}!")


name = func_1()
func_2()
print("name:", name)
