def solution(arr):
    smol = sorted(arr)[:1][0]
    print(smol)
    if smol in arr:
        arr.remove(smol)
    if len(arr)==0:
        arr.append(-1)
    return arr

solution([4,3,2,1])