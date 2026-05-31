# 1) Take the total withdrawal amount as input from the user and store it in `Amount`.
amount = int(input("Enter the amount of money you wish to withdraw: "))

# 2) Find how many 100-rupee notes are needed:
#    Divide `Amount` by 100 (whole number division) and store it in `note_1`.
note_100 = amount // 100

# 3) Find the remaining amount after taking out 100-rupee notes:
#    Use the remainder of `Amount` after dividing by 100.
amount %= 100

# 4) From the remaining amount, find how many 50-rupee notes are needed:
#    Divide the remainder by 50 (whole number division) and store it in `note_2`.
note_50 = amount // 50

# 5) Find the remaining amount after taking out 50-rupee notes:
#    Use the remainder after dividing by 50.
amount %= 50

# 6) From the remaining amount, find how many 10-rupee notes are needed:
#    Divide the remainder by 10 (whole number division) and store it in `note_3`.
note_10 = amount // 10

# 7) Print the number of 100-rupee notes, 50-rupee notes, and 10-rupee notes.
print("The number of Rs.100 notes = ", note_100)
print("The number of Rs.50 notes = ", note_50)
print("The number of Rs.10 notes = ", note_10)