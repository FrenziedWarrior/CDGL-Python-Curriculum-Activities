# ACTIVITY 2 - APPLICATION OF LOGICAL NOT OPERATOR IN PYTHON

a = 10
b = 20
c = 30

# Use not to reverse the result of a == b
print(not (a == b))

# Use not to reverse the result of b == c
print(not (b == c))

a = "apple"
b = "ball"

# Use not here to check if a and b are not equal
if not (a == b):
    print(a, 'and', b, 'are different')

a = 887
b = 45

# Use not here to reverse the result of comparing both conditions
if not ((a == 1) == (b == 5)):
    print("Hello")

a = int(input("Enter a number: "))
# Use not here to check that the number is not even
if not (a % 2 == 0):
    print(a, "is an odd number")