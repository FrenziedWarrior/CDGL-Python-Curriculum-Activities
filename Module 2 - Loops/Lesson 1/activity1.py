# STUDENT CAN TAKE EXAM UNDER TWO CONDITIONS
# - Student should have attendance >= 75%
# - If attendance is low, Student should have a medical certificate

# Take input for the student's attendance
attendance = int(input("Enter the attendance of the student: "))

if attendance >= 75:   # Attendance Condition
    print("Allowed")
else:
    # Take input for the student to check if they have medical certificate
    medical_cause = input("Do you have a medical certificate? ").upper()
    
    # Check if they answered Y or N for medical certificate
    if medical_cause == 'Y':   # Medical Certificate Present
        print("Allowed")
    else:
        print("Not Allowed")