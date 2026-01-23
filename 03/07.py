age = input("Enter your age: ")

# if not age.isdigit() and int(age) < 0:
if age.isdigit() and int(age) > 0:
    age = int(age)
    if age <= 5:
        print("Milk")
    elif age <= 12:
        print("Juice")
    elif age < 18:
        print("Soda")
    # elif age >= 18 and age <= 100:
    elif age <= 100:
        print("Coffee")
    else:
        print("Invalid age")
else:
    print("Invalid age")
a = 10
b = 33

if a > 0 or b < 0:
    print("At least one condition is True")
