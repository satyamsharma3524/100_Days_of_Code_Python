student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}
for student in student_scores:
    grades = student_scores[student]
    if grades>=91 and grades<=100:
        student_scores[student] = "Outstanding"
    elif grades>=81 and grades<=90:
        student_scores[student] = "Exceeds Expectations"
    elif grades>=71 and grades<=80:
        student_scores[student] = "Acceptable"
    elif grades<=70:
        student_scores[student] = "Fail"

student_grades = student_scores

print(student_grades)