# ACTIVITY 4 - FIND IF NUMBER IS EVEN OR ODD

number = int(input("Enter a number - "))

# EVEN NUMBERS: REMAINDER WITH 2 IS ALWAYS 0
# ODD NUMBERS: REMAINDER WITH 2 IS ALWAYS 1

if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")