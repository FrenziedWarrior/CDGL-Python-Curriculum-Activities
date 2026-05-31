# ACTIVITY 3 - MEAN VALUE

mean_wrong = 38
wrong_entry = 36
correct_entry = 56
total_numbers = 40

sum = total_numbers * mean_wrong
print("The total sum of all the entries (before correction) =", sum)

corrected_sum = sum - wrong_entry + correct_entry
print("The correct sum (after correction) =", corrected_sum)

correct_mean = corrected_sum / total_numbers
print(f"The correct mean of all {total_numbers} numbers is {correct_mean}")