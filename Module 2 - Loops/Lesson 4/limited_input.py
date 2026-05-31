import readchar
import sys

print("Enter 3 characters: ", end='', flush=True)
user_input = ""

while len(user_input) < 3:
    char = readchar.readchar()
    # Echo the character to the console
    sys.stdout.write(char)
    sys.stdout.flush()
    user_input += char

print(f"\nFinal input: {user_input}")
