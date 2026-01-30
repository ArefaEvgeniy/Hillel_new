my_str = "Hello, World's this one's, is sister's NEW line"

print(my_str.title())
print(my_str.capitalize())

print(my_str.upper())
print(my_str.lower())
print(my_str)

a = my_str.lower()
print(a)

print(my_str.title().replace("'S", "'s", 2).replace("o", "A").replace("e", "EE"))

print(my_str.title().replace("'S", "'s").count('s'))
