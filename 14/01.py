from dir_01.example import MyClass as MyClass01
from dir_02.example import MyClass as MyClass02


my_obj = MyClass01("Alice")
print(my_obj.greet())

my_obj = MyClass02("Bob")
print(my_obj.greet())
