# 1) Create variables to store different types of values:
#    - `name` as text (string)
#    - `age` as a whole number (integer)
#    - `is_student` as True/False (boolean)
#    - `weight` as a decimal number (float)
name = "Abhishek Karmakar"
age = 35
is_student = False
weight = 70.5

# 2) Print each variable’s value.
# 3) Print the datatype of each variable using `type()`.
print("Value of name = ", name)
print("Data type of name = ", type(name))

print("Value of age = ", age)
print("Data type of age = ", type(age))

print("Value of is_student = ", is_student)
print("Data type of is_student = ", type(is_student))

print("Value of weight = ", weight)
print("Data type of weight = ", type(weight))

# 4) Show a message that type casting will happen next.
print("Now taking care of Type Casting")

# 5) Convert `age` from an integer to a string and store it back in `age`.
age = str(age)

# 6) Print `age` and print its datatype again to confirm it changed.
print("Data type of age = ", type(age))

# 7) Convert `weight` from a float to an integer and store it back in `weight`.
weight = int(weight)

# 8) Print `weight` and print its datatype again to confirm it changed.
print("Data type of weight = ", type(weight))