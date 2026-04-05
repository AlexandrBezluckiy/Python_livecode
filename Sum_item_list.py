num_list = [1, 'a', 3.0, 4, 5.7, True, 7, 8, 9]

# sum = sum(num_list)
# print(sum)

sum2 = 0
for i in num_list:
    if isinstance(i, (int, float)):
        sum2 += i
    else:
        continue
print(sum2)