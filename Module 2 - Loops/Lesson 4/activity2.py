# ACTIVITY 2 : PRINT ALL PRIME NUMBERS BETWEEN 'LOWER' AND 'UPPER'

# 1) Take two integer inputs from the user and store them in `lower` and `upper`.
#    (These represent the starting and ending range.)

# 2) Print a message showing the range: from `lower` to `upper`.
lower = int(input("Lower: "))
upper = int(input("Upper: "))

# 3) Use a loop to check every number `num` from `lower` to `upper` (inclusive).
for i in range(lower, upper):
    is_prime = True

    if i > 1:
        for factor in range(2, i):
            if i % factor == 0:
                is_prime = False
                break

        if is_prime:
            print(i)

# 4) For each `num`, first check if it is greater than 1.
#    (Because prime numbers are always greater than 1.)

# 5) If `num` is greater than 1, test if it is prime:
#    a) Try dividing `num` by every number `i` from 2 to `num - 1`.
#    b) If `num` is divisible by any `i` (remainder is 0), it is NOT prime → stop checking (break).

# 6) If the loop finishes without finding any divisor (no break happened),
#    then `num` is prime → print `num`.