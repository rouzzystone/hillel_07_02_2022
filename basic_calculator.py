x = int(input("Enter the first digit:"))
y = int(input("Enter the second digit:"))

print('1. Add')
print('2. Substract')
print('3. Multiply')
print('4. Divide')

print('Enter the operation')
z = int(input())

if z == 1:
    a = x + y
elif z == 2:
    a = x - y
elif z == 3:
    a = x * y
elif z == 4:
    if y == 0:
        print("You cannot divide on zero, lol.")
        a = "N/A"
    else:
        a = x / y
else:
    print("We don't support that")
print("Result:")
print(a)






