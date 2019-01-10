# input
# 5
# ID         MARKS      NAME       CLASS     
# 1          97         Raymond    7         
# 2          50         Steven     4         
# 3          91         Adrian     9         
# 4          72         Stewart    5         
# 5          80         Peter      6   

# output
# 78.00

from collections import namedtuple

n = int(input())
students = []
sum_marks = 0
columns = ','.join(list(input().split()))
for i in range(n):
    one, two, three, four  =  input().split()
    Student = namedtuple('Student', columns)

    student = Student(one, two, three, four)
    students.append(student)

for student in students:
    sum_marks += int(student.MARKS)
print(float(sum_marks) / float(n))
