# Take input
print("Mirrored Pattern of Stars (*):")

rows = int(input("Enter number of rows - "))

for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end="")
    
    print("*" * (1+i))