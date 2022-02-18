x = [1, 2, 3, 4, 5, 6, 7]

y = len(x)

index = y // 2
if y % 2 > 0:
    index_2 = index + 1
    lst_1 = x[:index_2]
    lst_2 = x[index_2:]
else:
    lst_1 = x[:index]
    lst_2 = x[index:]

lst_3 = [lst_1, lst_2]


print(lst_3)

