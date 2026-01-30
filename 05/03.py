my_str = "     Hello,     World's this   one's,          is   sister's NEW     liHe..."

print(my_str)
print(my_str.strip('. liHe'))
print(my_str.strip('. ').replace('o', ''))

print(my_str.split())
print(my_str.split('s'))
print(my_str.split('is'))

new_list = my_str.split()
print(new_list)
new_str = ' '.join(new_list)
print(new_str)
