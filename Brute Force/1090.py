tc = int(input())
row = [map(int, input().split()) for _ in range(tc)]
answer = []

for i in range (tc):
    min = 0
    a, b = row[i]
    for x in range(1, 1_000_001):
        for y in range(1, 1_000_001):
            distance = abs(a - x) + abs(b - y)
            if distance < min:
                min = distance 
    answer[i] = min

print(*answer)