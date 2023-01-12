import sys
input = sys.stdin.readline

N = int(input())                            # 사람 수                    
names = list(input().split())               # 이름 저장
M = int(input())                            # 정보의 수
ancestors = {name: [] for name in names}    # 부모를 포함한 조상을 저장할 딕셔너리
levels = {name: 0 for name in names}        # 본인의 레벨(몇대 자손인지, 조상이 몇명인지)을 저장할 딕셔너리
children = {name: [] for name in names}     # 자손의 이름 저장할 딕셔너리

# 모든 사람의 조상을 딕셔너리에 저장하고 레벨 갱신
for _ in range(M):
    c, p = input().split()
    ancestors[c].append(p)
    levels[c] += 1

# print(ancestors)          {'daeil': ['sangdo'], 'sangdo': [], 'yuri': ['minji'], 'hoseok': ['sangdo', 'daeil'], 
#                           'minji': [], 'doha': ['minji'], 'haeun': ['doha', 'minji']}
# print(level)              {'daeil': 1, 'sangdo': 0, 'yuri': 1, 'hoseok': 2, 'minji': 0, 'doha': 1, 'haeun': 2}

# 모든 사람을 돌며 본인의 조상 중에서 "본인의 레벨에서 -1의 레벨을 가지고 있는" 부모님 찾아서 자식으로 넣기
for name in names:
    level = levels[name]
    # 본인이 선조이기 때문에 제외
    if level == 0:
        continue
    # 본인의 선조들 중에서 본인의 부모님 찾기
    for ancestor in ancestors[name]:
        if levels[ancestor] == level - 1:
            # 부모님의 자식으로 저장하기
            children[ancestor].append(name)
            break

# level이 0인 사람을 찾아 root로 저장.
root = dict(filter(lambda item: item[1] == 0, levels.items()))
print(len(root))
print(*sorted(list(root.keys())))

# 자식 정보 출력
for name in sorted(names):
    print(name, len(children[name]), *sorted(children[name]))