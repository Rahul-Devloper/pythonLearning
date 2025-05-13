def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


value = multiply(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(value)