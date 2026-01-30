str_1 = "Hello"
str_2 = "World"

print(str_1 + " " + str_2 + "!")
print(str_1)
print(str_2)
new_str = str_1 + " " + str_2 + "!"
print(new_str)
print(new_str * 3)  # new_str + new_str + new_str
print(3 * new_str)
print(len(new_str))
new_str += "\n new"  # new_str = new_str + "\n new"
print(new_str)
print(len(new_str))

print(new_str[:10:2])

print("-" * 50)
for item in new_str:
    print(item)
