# ACTIVITY 1 - SUM OF NATURAL NUMBERS

n = int(input("Enter a number until which you wish to calculate sum of whole numbers: "))

sum = 0

for i in range(1, n+1):
    sum = sum + i

print(f"The sum of first {n} natural numbers = {sum}")