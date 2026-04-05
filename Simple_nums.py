num = int(input("Введите число: "))

def validate(num):
    if num <= 0:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range (3, int((pow(num, 0.5) + 1))):
        if num % i  != 0:
            return True
    return True