user = input("Put your grade:")

def check_grade(grade):
    if grade > 80-100:
     return "You did a great job!"
    elif grade < 70-79:
     return "Keep it up!"
    elif grade < 60-69:
     return "You passed, but there's room for improvement."
    elif grade < Below 50:
     return "Better luck next time"

print(check_grade(10))