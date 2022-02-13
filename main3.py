x = input("Submit 5 digit number")

if x >= 100000:
    print("The number is not 5 digit")
elif x < 10000:
    print("The number is not 5 digit")
else:
    b, c = divmod(x, 10000)
    d, e = divmod(c, 1000)
    f, g = divmod(e, 100)
    y, z = divmod(g, 10)
    z = z * 10000
    y = y * 1000
    f = f * 100
    d = d * 10
    print(z + y + f + d + b)