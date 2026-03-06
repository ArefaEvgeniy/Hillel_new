class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def __str__(self):
        msg = "Cat [ name = {}, age = {}, color ={}]"
        return msg.format(self.name, self.age, self.color)

    def __getattribute__(self, atr_name):
        """ Робити перехоплення винятку у цьому методі, не
				зовсім коректно.
        Більш правильний підхід - реалізувати роботу з полями,
        яких немає, у методі __getattr__"""
        try:
            return object.__getattribute__(self, atr_name)
        except AttributeError:
            return None


cat = Cat('Barsik', 3, 'black')
print(cat.name)  # виведе Barsik

# Звернення до поля, якого немає
print(cat.type)  # виведе  None
