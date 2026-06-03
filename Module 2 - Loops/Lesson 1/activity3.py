print("Select your ride: ")
print("1. Pizza")
print("2. Biryani")

# take input of number 1 or 2
# select your ride
choice = int(input("Enter your choice: "))

# User entering option 1
if (choice == 1):  # condition 1 outer if statement
    print("what type of Pizza? ")
    print("1.Paneer\n")
    print("2.Chicken\n")

    # Condition for selecting the type of bike
    choice2 = int(input("Enter you choice2: "))
    if choice2 == 1:  # inner if statement
        print("you have selected Paneer Pizza")
    else:
        print("you have selected Chicken Pizza")

# User entering option 2
elif (choice == 2):  # outer elif statement
    print("what type of Biryani?")
    print("1.Veg")
    print("2.Chicken")
    choice3 = int(input("enter your choice3: "))

    if choice3 == 1:  # inner if statement
        # condition for selecting the type of car
        print("you have selected Veg Biryani")
    else:
        print("you have selected Chicken Biryani")

else:  # outer else statement
    print("Wrong choice!")
