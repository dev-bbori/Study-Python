# 학생 클래스
# 이름(name), 학년(grade), 과목별 성적(scores)
# 주어진 과목명과 성적을 받아서, 해당 과목의 성적을 저장한다.
# 학생의 전체 과목의 평균 성적을 계산한다


class Student:

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.scores = {}

    def set_score(self, subject, score):
        self.scores[subject] = score

    def get_average(self):
        total_score = sum(self.scores.values())
        avg_score = total_score / len(self.scores)
        return total_score, avg_score


student = Student('허은상', 4)
student.set_score("math", 100)
student.set_score("kor", 50)
student.set_score("eng", 90)

print(student.name)
print(student.get_average())