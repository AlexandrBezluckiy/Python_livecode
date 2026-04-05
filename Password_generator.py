import random

lenth = int(input("Введите длину пароля: "))
password = ''
vocabular = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+-=[]{}|;:,.<>/?"
temp_list = list(vocabular)
random.shuffle(temp_list)

if lenth < 0:
    lenth = 0

for num in range(lenth):
    password.join(random.choice(temp_list))

print(password)

