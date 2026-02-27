class Dog:
    def say(self):
        return "Woof!"

    def go(self):
        return "The dog is running."

    def eat(self):
        return "The dog is eating."

    def stay(self):
        return "The dog is staying still."


class Dolphin:
    def say(self):
        return "Click-click!"

    def go(self):
        return "The dolphin is swimming."

    def eat(self):
        return "The dolphin is eating fish."

    def jump(self):
        return "The dolphin is jumping out of the water!"

    def swim(self):
        return "The dolphin is swimming gracefully."


class Monster(Dolphin, Dog):
    pass


obj = Monster()
print(obj.swim())
print(obj.stay())
print(obj.say())
