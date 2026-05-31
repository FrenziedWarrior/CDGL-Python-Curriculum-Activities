character = input("Enter any 1 character: ")

# print(ord("a"), ord("z"), ord("A"), ord("Z"))

# if ord(character) >= 65 and ord(character) <= 90:
#     print("It is an alphabet")
# elif ord(character) >= 97 and ord(character) <= 122:
#     print("It is an alphabet")
# else:
#     print("It is not an alphabet")


if character >= "a" and character <= "z":
    print("It is an alphabet")
elif character >= "A" and character <= "Z":
    print("It is an alphabet")
else:
    print("It is not an alphabet")
