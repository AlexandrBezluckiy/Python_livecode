num = int(input("Введите неотрицательное целое число: "))

def factorial(num):
    if num <= 0:
        return None
    fack = 1
    for i in range(1, num + 1):
        fack *= i
    return fack

print(factorial(num))