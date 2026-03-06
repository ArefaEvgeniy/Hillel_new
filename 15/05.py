class Human:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def full_name(self):
        return f"{self.name} {self.surname}"

    @full_name.setter
    def full_name(self, value):
        self.name, self.surname = value.split()

    @full_name.deleter
    def full_name(self):
        self.name = None
        self.surname = None
        print("Hello, Dmytro!")


men = Human("John", "Doe")
print(men.name)
print(men.surname)
print(men.full_name)

print("-----------")
men.surname = "Smith"
print(men.name)
print(men.surname)
print(men.full_name)

# a = men.full_name
# print(a)
# print(type(a))

men.full_name = "Inna Shyshova"
print("-----------")
print(men.name)
print(men.surname)
print(men.full_name)

del men.full_name
print("-----------")
print(men.name)
print(men.surname)
print(men.__dict__)
