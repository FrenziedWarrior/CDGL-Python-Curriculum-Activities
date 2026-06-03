# ACTIVITY 1 - SUM OF N NATURAL NUMBERS

n = int(input("Enter the value of terms: "))

# to hold the running sum
sum = 0

# loop index
i = 1

# loop will run from 1 to n
while i <= n:
  sum += i
  i += 1

print("\nSum =", sum)