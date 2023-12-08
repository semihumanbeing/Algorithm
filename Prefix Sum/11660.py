graph = [list(map(int,input().split())) for _ in range (4)]
x1, y1, x2, y2 = map(int, input().split())

# 2차원 배열 만들기 graph 보다 하나 크게
prefix =[ [0 for _ in range(5)] for _ in range(5)] 

# 2차원 배열 prefix 
# 현재 위치에서 한 칸 왼쪽과 한칸 위의 값을 더해준 뒤 
# 중복으로 더한 값을 뺀 것에 graph 현재 값 넣기
for y in range(4):
    for x in range(4):
        prefix[y+1][x+1] = prefix[y][x+1] + prefix[y+1][x] - prefix[y][x] + graph[y][x]

# [y2][x2] 는 [0][0] 부터 모든 범위이다
# [x1 -1], [y1 - 1] 을 빼 주고
# 중복으로 뺀 [y1 -1][x1 -1] 을 더해준다
print(prefix[y2][x2] - prefix[y2][x1-1] - prefix[y1-1][x2] + prefix[y1-1][x1-1])