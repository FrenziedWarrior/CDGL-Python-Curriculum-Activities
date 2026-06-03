# AFTER CLASS PROJECT - NESTED CONDITIONS
# Assignment: Check Age
# Write a program to check the age entered by the user is between 10 to 20 years or not?

age = int(input("Enter age: "))

if age >= 10:
    if age <= 20:
        print("Age is between 10 & 20 years")
    else:
        print("Age is not between 10 & 20 years")