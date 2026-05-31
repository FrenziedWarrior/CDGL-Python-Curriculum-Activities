# ACTIVITY 1 - AND-OR SEPARATOR

# 1) Store values in `a`, `b`, and `c`.
a = 100
b = 0
c = 57

# 2) Check an AND condition using `a and b and c`:
#    - This becomes True only if all three values are treated as True.
#    - If the condition is True, print the “all true” message.
#    - Otherwise, print the “at least one false” message.
if a and b and c:
    print("All numbers have Boolean value as True")
else:
    print("At least one number has Boolean value as False")


# 3) Re-assign (change) new values to `a`, `b`, and `c` for the next checks.
a = 199
b = 83
c = -10

# 4) Check an OR condition: `a > 0 or b > 0`
#    - If at least one of them is greater than 0, print the “either is greater than 0” message.
#    - Otherwise, print the “no number is greater than 0” message.
if a > 0 or b > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")

# 5) Check another OR condition: `b > 0 or c > 0`
#    - If at least one of them is greater than 0, print the “either is greater than 0” message.
#    - Otherwise, print the “no number is greater than 0” message.
if b > 0 or c > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")