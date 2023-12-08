import sys
input = sys.stdin.readline

N, H = map(int, input().split())
line = [0 for _ in range(H)]

# N크기만큼 돌기
for i in range(N):
    # 높이 입력
    height = int(input())
    # i 가 짝수이면 바닥 지점에 1 추가하고 꼭대기 기점에 1 빼기
    if i %2 == 0:
        line[0] += 1
        line[height] -= 1
    if i %2 == 1:
        # i가 홀수이면 전체 높이에서 장애물 높이를 뺀 부분에 1 추가
        line[H - height] += 1

prefix = [0 for _ in range(H + 1)]
for j in range(H):
    prefix[j + 1] = prefix[j] + line[j]

prefix = prefix[1:] # 리스트를 1번째부터 자르기
print(min(prefix), prefix.count(min(prefix)))

