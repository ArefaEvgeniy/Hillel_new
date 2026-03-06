class Student:
    def __eg__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)


obj_1 == obj_2
hash(obj_1) == hash(obj_2)


hash(Student("Alice"))
