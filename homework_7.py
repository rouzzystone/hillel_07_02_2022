x = [0, 0, 2, 3, 8, 10, 13, 0, 9]
for l in range(len(x)):
    if x[l] == 0:
        x.remove(0)
        x.insert(-1, 0)
print(x)
