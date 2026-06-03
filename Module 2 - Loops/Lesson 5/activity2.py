# ACTIVITY 2 - FLOYD'S TRIANGLE

# Take input from user
rows = int(input("Please Enter the total Number of Rows  : "))
number = 1  # initialise by 1

print("Floyd's Triangle")

# outer loop for number of rows
for i in range(rows):
    # inner loop for number of columns
    for j in range(i + 1):
        # display result
        print(number, end='  ')
        number = number + 1
    print()
