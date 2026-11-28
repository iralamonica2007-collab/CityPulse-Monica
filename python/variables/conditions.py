# EXAM GRADE CALCULATOR

marks = int(input("Enter your marks (0-100): "))

if marks >= 90:
    print("Grade A - Excellent!")
elif marks >= 75:
    print("Grade B - Very good!")
elif marks >= 50:
    print("Grade C - You passed.")
elif marks >= 35:
    print("Grade D - Just passed, work harder.")
else:
    print("Grade F - Failed. Try again!")