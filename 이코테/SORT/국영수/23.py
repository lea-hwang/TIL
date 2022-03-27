import sys
sys.stdin = open('23_input.txt', 'r')

N = int(input())                    # 학생수
students = []                       # 학생이름, 국어성적, 영어성적, 수학성적
for i in range(N):
    input_data = list(input().split())
    students += [[input_data[0]] + list(map(int, input_data[1:4]))]

students.sort(key=lambda student: (-student[1], student[2], -student[3], student[0]))


for student in students:
    print(student[0])


# 참고한 블로그
# https://gorokke.tistory.com/38

# 오름차순으로 정렬
# -를 앞에 붙인다
