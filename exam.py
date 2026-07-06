student_name = "John"
marks = 82
attendance = 90
day = "sat"
club = "science"
fees_paid = True

if marks >= 90:
    print("Grade: A+")
elif marks >= 75:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
else:
    print("Grade: C")

if attendance >= 75 and fees_paid == True:
    print("Eligible for Exam")

    if day in ["sat", "sun"]:
        print("Weekend Special Class")

    if club == "science" or club == "math":
        print("Science Exhibition Allowed")
    else:
        print("Normal Classroom")

else:
    print("Not Eligible for Exam")

print("Thank you")