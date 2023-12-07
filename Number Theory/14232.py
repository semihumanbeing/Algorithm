n = int(input())
amount = 0
nums = []
for i in range(1, n):
    if i > 1 and n % i == 0:
        nums.append(i)
        amount += 1

print(amount)
print(*nums)
