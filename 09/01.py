def apply_operation(operation, data):
    """
    Застосовує вказану операцію до кожного елемента списку.

    :param operation: Функція-операція для застосування.
    :param data: Список даних.
    :return: Результат операції для кожного елемента списку.
    """
    result = []
    for item in data:
        result.append(operation(item))
    return result


# Приклад використання
def square(x):
    return x ** 2


def double(x):
    return x * 2


# def summa(x, y):
#     return x + y


numbers = [1, 2, 3, 4, 5]

squared_numbers = apply_operation(square, numbers)
doubled_numbers = apply_operation(double, numbers)
# summa_numbers = apply_operation(summa, numbers)

print(squared_numbers)  # [1, 4, 9, 16, 25]
print(doubled_numbers)   # [2, 4, 6, 8, 10]
