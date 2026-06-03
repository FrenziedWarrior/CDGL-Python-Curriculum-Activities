# ACP: Power calculator
# Write a program to calculate the n number power of a given number?

number = int(input("Enter the base: "))
power = int(input("Enter the power: "))

result = 1

for i in range(power):
    result *= number

print(f"{number} raised to the power {power} = {result}")