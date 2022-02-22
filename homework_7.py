x = [0, 0]
for l in range(len(x)):
    if x[l] == 0:
        x.remove(0)
        x.insert(-1, 0)
print(x)
