def factorial(n):
    """
    Обчислює факторіал числа n.

    :param n: Ціле число.
    :return: Факторіал числа n.
    """
    # Базовий випадок: 0! та 1! рівні 1
    if n == 0 or n == 1:
        return 1
    else:
        # Рекурсивний виклик: n! = n * (n-1)!
        return n * factorial(n - 1)

value = 955
print(factorial(value))

res = 1
while value > 0:
    res = res * value
    value -= 1

print(res)  # Виведе 120

