# ACTIVITY 1 - Half Pyramid Pattern of Stars (*)

# Take input
print("Half Pyramid Pattern of Stars (*):")

rows = int(input("enter the number of rows: "))

# outer loop to handle number of rows
for i in range(rows):
    # inner loop to handle number of columns
    for j in range(i + 1):
        # display result
        print("* ", end="")
    print()