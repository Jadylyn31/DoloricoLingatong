grade = int(input("Put your grade:"))


def check_grade(grade):
    if grade >= 80 and grade <= 100:
        return "You did a great job!"
    elif grade >= 70 and grade <=79:
        return "Keep it up!"
    elif grade >= 60 and grade <= 69:
        return "You passed, but there's room for improvement."
    elif grade >= 50:
        return "Better luck next time"
   

print(check_grade(grade))