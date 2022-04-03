words2 = []
queries2 = []

N = 0
M = 0
cnt = []

sorted_list = []
reversed_list = []


def binary_search(start, end, k):  # start, end 단어 순서, pattern 매칭할 패턴 순서
    if start <= end:
        mid = (start + end) // 2
        if queries2[k][0] == '?':  # 뒤에서부터 탐색
            pattern = list(reversed(queries2[k]))
            word = reversed_list[mid]
        else:
            pattern = queries2[k]
            word = sorted_list[mid]
        for idx in range(len(pattern)):  # 한글자씩 비교
            if pattern[idx] == '?':  # 패턴이 일치할 경우
                if len(pattern) == len(word):
                    cnt[k] += 1
                binary_search(start, mid - 1, k)
                binary_search(mid + 1, end, k)
                break

            if word[idx] != pattern[idx]:
                if ord(word[idx]) < ord(pattern[idx]):  # 패턴이 더 뒤에 있을때, 오른쪽 탐색
                    binary_search(mid + 1, end, k)
                else:  # 왼쪽 탐색
                    binary_search(start, mid - 1, k)
                break


def solution(words, queries):
    global N, M, cnt, sorted_list, reversed_list, queries2
    N = len(words)  # 단어의 수
    M = len(queries)  # 패턴의 수
    queries2 = queries
    cnt = [0] * M

    sorted_list = sorted(words)  # 단어 사전순 정렬
    reversed_list = sorted([list(reversed(word)) for word in words])  # 뒤집은 단어 사전순 정렬

    for k in range(M):
        binary_search(0, N - 1, k)

    return cnt