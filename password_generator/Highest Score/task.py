student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

score = 0
for student in student_scores:
    if student > score:
        score = student

print(score)