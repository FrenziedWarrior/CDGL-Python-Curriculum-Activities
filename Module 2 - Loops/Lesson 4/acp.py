# ACP - DECIMAL TO BINARY CONVERSION

# Take a variable num and assign any positive number to it
num = 23

# Create an empty-string variable - binary
# This will hold the final "answer"
binary = ""

# Store the original number for printing later
original = num

# Run while loop - as long as n does not go below 0
while num > 0:

    # Get remainder (by 2)
    remainder = num % 2

    # Add the remainder to the answer variable created above
    binary = binary + str(remainder)

    # Floor division to reduce n
    num = num // 2

# Reverse the string to get the correct binary representation
binary = binary[::-1]

# Print the answer
print("The binary number for", original, "is", binary)