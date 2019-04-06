n, x = (int(x) for x in input().split())

subject_marks = []
for _ in range(x):
    subject_marks.append([float(x) for x in input().split()])

student_marks = zip(*subject_marks)
average = [(sum(marks)/x) for marks in student_marks]
print(*average, sep='\n')