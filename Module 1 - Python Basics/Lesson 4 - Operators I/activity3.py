# 1) Ask the user to enter marks for 4 subjects: math, english, science, and hindi.
#    Store each mark in its own variable.
math_marks = int(input("Enter marks for Maths: "))
english_marks = int(input("Enter marks for English: "))
science_marks = int(input("Enter marks for Science: "))
hindi_marks = int(input("Enter marks for Hindi: "))

# 2) Add all 4 subject marks and store the total in `sum`.
sum = math_marks + english_marks + science_marks + hindi_marks

# 3) Print the total marks stored in `sum`.
print("The total marks are:", sum)

# 4) Calculate the percentage:
#    - Divide `sum` by 400 (total maximum marks for 4 subjects, assuming each is out of 100)
#    - Multiply the result by 100
#    Store the final value in `perc`.
perc = (sum/400) * 100

# 5) Print the percentage stored in `perc`.
print("Percentage secured: ", perc)