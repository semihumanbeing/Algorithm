N = int(input())
answer = 0
# 0부터 N 까지 돌면서 각 자리수를 더함
for i in range (N):
    arr = list(map(int, str(i)))
    check = i + sum(arr)
    if check == N:
        answer = i
        break
print(answer)
    

# 만약에 N이 나오면 break
