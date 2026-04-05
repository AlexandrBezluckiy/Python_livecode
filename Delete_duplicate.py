my_list = ['one', 'two', 'three', 'one', 'five', 'two']

new_list = []
for item in my_list:
    if item in new_list:
        continue
    else:
        new_list.append(item)
print(new_list)