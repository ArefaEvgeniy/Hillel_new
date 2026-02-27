class MyClass:
    @staticmethod
    def summa(a, b):
        return a + b

    def new_summa(self, a, b):
        return self.summa(a, b) + 10

    @staticmethod
    def multiply(a, b):
        return a * b


obj = MyClass()
print(obj.summa(2, 3))
print(obj.multiply(2, 3))

print("------------------")
print(MyClass.multiply(2, 3))
