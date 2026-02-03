my_str = "Мій рідний край"
my_str_2 = "São Paulo ça ño"


bytes_1 = my_str_2.encode()
bytes_2 = my_str_2.encode("utf-16")
bytes_3 = my_str_2.encode("Latin-1")

print(bytes_1)
print(len(bytes_1))
print(bytes_2)
print(len(bytes_2))
print(bytes_3)
print(len(bytes_3))

print(bytes_1.decode("utf-8"))
print(bytes_2.decode("utf-16"))
print(bytes_3.decode("Latin-1"))

bytes_10 = my_str.encode("utf-8")
# bytes_11 = my_str.encode("Latin-1")

print(bytes_10)
print(len(bytes_10))

# print(bytes_11)
# print(len(bytes_11))


str_1 = "A"
str_2 = "А"

print(str_1 == str_2)  # False

print(ord(str_1))  # 65
print(ord(str_2))  # 1040

print(str_1.encode())
print(str_2.encode())

рrint(chr(1040))
