# Project 5: CHECK TEMPERATURE FOR SUGGESTING LIGHT CLOTHES
# Light >= 20, 
# Medium >= 15 , 
# Warm < 15

temperature = float(input("Enter temperature: "))

if temperature >= 20:
    print("Light clothes")
elif temperature >= 15:
    print("Medium clothes")
else:
    print("Warm clothes")