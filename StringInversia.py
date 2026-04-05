stroka = input("Введите строку: ")
print(stroka[::-1])

new_word = ''
for i in range(len(stroka)):
    new_word += stroka[len(stroka) - (i+1)]
print(new_word)

print(''.join(reversed(stroka)))