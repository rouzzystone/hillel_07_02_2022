x = input("Submit the number")
if x >= 10000:
    print("Submit 4 digit number")
elif x <= 1000:
    print("Submit 4 digit number")
else:
    y, z = divmod(x, 1000)
    a, b = divmod(z, 100)
    c, d = divmod(b, 10)
    print(y)
    print(a)
    print(c)
    print(d)
