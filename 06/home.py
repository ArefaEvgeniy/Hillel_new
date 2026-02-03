import string
import keyword


cycle = "y"

while cycle not in ("y", "yes", "т", "так"):

    ...

    cycle = input("Продовжити? (y/yes/т/так): ").lower()
    # if cycle == "y" or cycle == "yes" or cycle == "т" or cycle == "так":
    # if cycle not in ("y", "yes", "т", "так"):
    #     break


my_str = 'True'
print(string.punctuation)
for item in string.punctuation + " ":
    print(item)
    if item in my_str:
        print('Find')

if my_str in keyword.kwlist:
    print('!!!!')

new_list = []
for _ in ["y", "yes", "т", "так"]:
    new_list.append(0)

print(new_list)

import random

random_list = [random.randint(1, 100) for _ in range(random.randint(3, 10))]
print(random_list)
