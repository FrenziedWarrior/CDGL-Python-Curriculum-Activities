# ACTIVITY 1 - IDENTITY OPERATOR
# Python program to illustrate the use of "is" operator

x = 5

# print("type(x) == int ->", type(x) == int, type(int))
# print(type(type))

if (type(x) is int):
    print("true")
else:
    print("false")

x = 5.5

if (type(x) is not float):
    print("true")
else:
    print("false")

x = "Abhishek"
y = "Abhishek"

if (x is y):
    print("x & y SAME identity")

# y = 30
if (x is not y):
    print("x & y have DIFFERENT identity")