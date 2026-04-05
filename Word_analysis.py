stroka = "The quick brown fox jumps over the lazy dog. The dog was lazy."
stroka = stroka.lower()

new_list = stroka.split(" ")
sign = ',.!?'
for item in new_list:
    index = new_list.index(item)
    if item[-1] in sign:
        item = item[0:-1]
    new_list[index] = item

new_dict = {}
for item in new_list:
    if new_dict.get(item) == None:
        new_dict[item] = 1
    else:
        new_dict[item] += 1
print(new_dict)