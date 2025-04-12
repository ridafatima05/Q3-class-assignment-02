#GRADING SYSTEM 
#ASSIGNMENT 02 PART 2

print("Welcome to Rida Fatima's Grading System")
def grading_system():
    try:
        score = int(input("Enter your Total Score out of 100: "))

        if score < 0 or score > 100:
            print("Invalid score. Please enter a number between 0 and 100.")
        elif score >= 90:
            print("Grade: A+")
        elif score >= 80:
            print("Grade: A")
        elif score >= 70:
            print("Grade: B+")
        elif score >= 60:
            print("Grade: C+")
        elif score >= 50:
            print("Grade: D+")
        else:
            print("Grade: F")

    except ValueError:
        print("Invalid input. Please enter a numeric value.")


grading_system()
