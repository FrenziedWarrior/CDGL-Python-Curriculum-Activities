# ACTIVITY 3 - ARMSTRONG NUMBER

# 1) Ask the user to enter a number and store it in `num`.
num = int(input("enter a number - "))

# 2) Set `sum` to 0.
#    (This will store the total of the cubes of each digit.)
sum = 0

# 3) Copy `num` into `copy`.
#    (We will change `copy` while checking digits, but we must keep `num` unchanged.)
copy = num

# 4) Repeat while `copy` is greater than 0:
while copy > 0:
    #    a) Find the last digit of `copy` and store it in `digit`.
    digit = copy % 10
    
    #    b) Add (digit ** 3) to `sum`.
    sum = sum + (digit ** 3)

    #    c) Remove the last digit from `copy` so you can move to the next digit.
    copy = copy // 10

# 5) After the loop, compare `num` and `sum`:
#    - If they are the same, print: `num` is an Armstrong number.
#    - Otherwise, print: `num` is not an Armstrong number.
if num == sum:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")