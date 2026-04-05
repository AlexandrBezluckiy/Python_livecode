stroka = input("Введите строку: ")
stroka_to_list = list(stroka.split(' '))
print(stroka_to_list)

max_item = stroka_to_list[0]
for item in range(len(stroka_to_list)):
    if len(max_item) < len(stroka_to_list[item]):
        max_item = stroka_to_list[item]
    else:
        continue
print(max_item)