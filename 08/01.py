name = "Bob"


def func_1():
    global name
    name = "Alice"
    print(f"Hello, {name}!")


def func_2():
    def func_3():
        print(f"Hi, {name}!")

    name = "Charlie"
    func_3()
    print(f"Goodbye, {name}!")


func_1()
func_2()
print("name:", name)
