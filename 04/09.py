
while True:
    number = input("Enter a number: ")
    if number.isdigit():
        number = int(number)
        break
    print("Invalid input. Please enter a valid number.")

print(number)
