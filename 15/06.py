class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def __str__(self):
        msg = "Cat [ name = {}, age = {}, color ={}]"
        return msg.format(self.name, self.age, self.color)

    def __getattr__(self, atr_name):
        return "Такого атрибута не має"


cat = Cat('Barsik', 3, 'black')
print(cat.name)  # виведе Barsik

# Звернення до поля, якого немає
print(cat.type)  # виведе  None
