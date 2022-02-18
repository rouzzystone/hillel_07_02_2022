x = []
if len(x) == 0:
    print(x)
else:
    y = x[-1]
    x.insert(0, y)
    x.pop()
    print(x)