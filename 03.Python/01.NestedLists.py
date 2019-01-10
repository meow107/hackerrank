from operator import itemgetter

students = []
scores = []


for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    scores.append(score)
    student = [name,score]
    students.append(student)


unique_scores = list(set(scores))
unique_scores.sort()

n_student = len(students)
i = 0
students.sort(key=itemgetter(0),reverse=False)

while i < n_student:
    student = students[i]
    if student[1] == unique_scores[1]:
        print(student[0])
    i += 1

