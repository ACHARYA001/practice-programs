if __name__ == '__main__':
    records = []
    for student in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    
    marks = [i[1] for i in records]
    # print(marks)
    sec_low_mark = min([k for k in marks if k != min(marks)])
    # print(sec_low_mark, marks)
    
    students = [j[0] for j in records if j[1] == sec_low_mark]
    students.sort()
    for studnt in students:
        print(studnt)