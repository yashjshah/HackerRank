from collections import namedtuple

rows = int(input())
columns = input().split()
Student = namedtuple('Student', columns)

sum_marks = 0
for _ in range(rows):
    field = input().split()
    student = Student(*field)
    sum_marks += int(student.MARKS)
print("{:.2f}".format(sum_marks/rows))

