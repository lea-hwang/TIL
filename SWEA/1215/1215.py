import sys
sys.stdin = open('input.txt', 'r')

def count_palindrome(letters, word_len):
    count = 0
    for i in range(8):                          # 모든 행을 돌 동안
        for j in range(9 - word_len):           # 첫번째부터 시작해서
            word = letters[i][j:j + word_len]   # 길이가 word_len만큼인 단어를 슬라이싱한다.
            # 그 단어를 반으로 쪼갠다
            left = word[:word_len // 2]         # 짝수면 :4//2 홀수면 5//2
            right = word[(word_len + 1) // 2:]  # 짝수면 : 2:, 홀수면 3:
            if list(reversed(left)) == right:   # 왼쪽 리스트를 뒤집었을 때 오른쪽 리스트와 같다면 # reversed는 하고나서 list를 씌워줘야함
                count += 1
    return count

T = 10
for tc in range(1, T+1):
    word_len = int(input()) # 회문의 길이
    letters = [list(input()) for i in range(8)] # 글자판
    count = 0
    # 가로 방향 회문 세기
    count += count_palindrome(letters, word_len)
    # 세로 방향 회문 세기
    letters = list(map(list, zip(*letters)))
    count += count_palindrome(letters, word_len)

    print(f'#{tc} {count}')