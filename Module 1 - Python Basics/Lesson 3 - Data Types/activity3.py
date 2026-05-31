# 0 1 2 3 4 5 6 7 8 9 10 11 12 13
# A b h i s h e k   K a r

# 1) Ask the user to enter a word or sentence and store it in `text`.
# 2) Reverse the string stored in `text` and store the reversed result in `revText`.
#    (Reversing means the last character becomes first, and the first becomes last.)
# 3) Replace `text` with the reversed string (set `text` equal to `revText`).
# 4) Print a message saying you are showing the reversed string.
# 5) Print the reversed string stored in `text`.

text = input("Enter a string: ")

# [ START_INDEX : END_INDEX : SKIP]
revText = text[::-1]

text = revText

print("Reversed text is", text)

string = "ABCD".lower()