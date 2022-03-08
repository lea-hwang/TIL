import sys
sys.stdin = open('14544_input.txt', 'r')

P = int(input())
for i in range(1, P+1):
    n, m = map(int, input().split()) # 후보수
    candidates = {input(): 0 for _ in range(n)} # 후보 이름
    for _ in range(m):
        name, count, center = input().split()
        candidates[name] += int(count)

    top = max(candidates.values())
    top_candidate = []
    for candidate, value in candidates.items():
        if value == top:
            top_candidate.append(candidate)

    if len(top_candidate) == 1:
        print(f'VOTE {i}: THE WINNER IS {top_candidate[0]} {top}')
    else:
        print(f'VOTE {i}: THERE IS A DILEMMA')
