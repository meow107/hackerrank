if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()

    score_list = student_marks[query_name]
    percentage = 0
    n_score = len(score_list)
    for item in score_list :
        percentage += item
    
    print(("%0.2f") % (percentage / n_score))






