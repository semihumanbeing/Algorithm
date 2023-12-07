N = int(input())
arr = list(map(int, input().split()))
prefix = [0 for _ in range(N+1)]
isneg = 0
if max(arr) < 0: isneg = 1

for i in range(1, N):
    prefix[i] = max(prefix[i-1] + arr[i], arr[i])
print(prefix)
if len(arr) == 1 : 
    print(arr[0])
elif isneg == 1 and 0 in arr:
    print (0)
elif isneg == 1:
    print(max(arr))
else :
    print(max(prefix))
