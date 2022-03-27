import sys
sys.stdin = open('3_input.txt', 'r', encoding='utf-8')

N = int(input())                                # 학생 수

students = []                                   # 학생의 이름과 성적을 담을 리스트
for _ in range(N):
    person = list(input().split())              # 학생 정보
    students.append([person[0], person[1]])     # 리스트에 담기

students.sort(key=lambda x:x[1])                # 정렬

for student in students:
    print(student[0], end=" ")
