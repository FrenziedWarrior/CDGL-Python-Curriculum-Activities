# ACTIVITY 1 - OPERATOR PRECEDENCE

# 1) Store values in `v`, `w`, `x`, `y`, and `z`.
v = 10
w = 20
x = 30
y = -15

# 2) Calculate the expression (v + w) * x / y and store the result back in `z`.
z = (v + w) * x / y

# 3) Print the value of `z` with a message.
print("The value of the expression (v + w) * x / y = ", z)

# 4) Store a name in `name` and a number in `age`.
name = "Alex"
age = 35

# 5) Check this condition using `or` and `and`:
#    - The code checks if `name` is "Alex"
#      OR (if `name` is "John" AND `age` is 2 or more).
#    - If the condition is true, print the welcome message.
#    - Otherwise, print the goodbye message.
if name == "Alex" or name == "John" and age >= 2:
    print("Welcome,", name)
else:
    print("Good Bye!")