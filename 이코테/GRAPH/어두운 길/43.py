

# N개의 집과 M개의 도로로 구성
# 0번부터 N-1까지의 번호로 구분
# 가로등을 켜기 위한 비용은 집 사이의 거리와 동일
# 일부 가로등을 비활성화하여 절약할 때 그 최대 금액


N, M = map(int, input().split())
distance = []
for _ in range(M):
    X, Y, Z = map(int, input().split())
    distance[X].append((Y, Z))