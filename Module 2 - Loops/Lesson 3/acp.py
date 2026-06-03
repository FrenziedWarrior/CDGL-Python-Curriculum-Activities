# ACP - Write a program to calculate how many total digits are in a number entered by the user

# 1) Ask the user to enter a number and store it in `num`.
num = int(input("Enter a number - "))

# 2) Set `count` to 0.
#    (This will store the total count of digits in given number.)
count = 0

copy = num

# 3) Repeat while `copy` is greater than 0:
while copy > 0:
    #    a) Find the last digit of `copy` and store it in `digit`.
    digit = copy % 10
    
    #    b) Add 1 to `count`.
    count += 1

    #    c) Remove the last digit from `copy` so you can move to the next digit.
    copy //= 10

# 5) After the loop, print the total count of digits
print(f"Total number of digits in {num} = {count}")