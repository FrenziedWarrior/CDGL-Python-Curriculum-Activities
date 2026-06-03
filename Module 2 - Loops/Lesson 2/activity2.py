# ACTIVITY 2 - REVERSE A STRING

string = input("Enter any string: ")

string2 = ""

for character in string:
    string2 = character + string2

print("The original string =", string)
print("The reversed string =", string2)