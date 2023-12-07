import math
# 공약수열
tc = int(input())
nums = sorted(map(int, input().split()))
count = 0

# tc 안, nums의 범위 내에서 nums(tc) 의 하나 전 인덱스와 i의 값을비교한다
# 만약 최대공약수가 1이면 이후 인덱스랑 비교한다
def check(a,b):
    for i in range(a, b):
        if math.gcd(a, i) == 1 and math.gcd(i, b) == 1:
            return 1
    return 2

for a in range(1, tc):
    # 최대공약수가 1이면 ok 비교해서 1이 아니면
    if math.gcd(nums[a], nums[a-1]) != 1:
        count += check(nums[a-1], nums[a])
        
        
print(count)