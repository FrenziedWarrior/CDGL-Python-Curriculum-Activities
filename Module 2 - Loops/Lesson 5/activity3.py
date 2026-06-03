# ACTIVITY 3 - Diamond Pattern

# Take input from user
rowSize = int(input("enter the number of rows: "))

if rowSize % 2 == 0:  # conditions
    halfDiamRow = int(rowSize/2)
else:
    halfDiamRow = int(rowSize/2)+1

spaces = halfDiamRow-1

# Loop for upper part
for i in range(1, halfDiamRow+1):  # loop for rows
    for j in range(1, spaces+1):  # loop for columns
        print(end=" ")
    spaces = spaces-1
    num = 1
    for j in range(2*i-1):
        print(end=str(num))
    # incerementing number at each column
        num = num+1
    print()
spaces = 1


# Loop for lower part
for i in range(1, halfDiamRow):  # loop for rows
    for j in range(1, spaces+1):  # loop for columns
        print(end=" ")
    spaces = spaces+1
    num = 1
    for j in range(1, 2*(halfDiamRow-i)):
        print(end=str(num))  # display result
    # incerementing number at each column
        num = num+1
    print()
