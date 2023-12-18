def solution(answers):
    answer = []
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    sMap = {1:0,2:0,3:0}
    
    idx1 = 0
    idx2 = 0
    idx3 = 0
    for i in range(len(answers)):
        if idx1 > len(s1) -1:
            idx1 = 0
        if idx2 > len(s2) -1:
            idx2 = 0
        if idx3 > len(s3) -1:
            idx3 = 0
            
        if answers[i] == s1[idx1]:
            sMap[1] += 1
        if answers[i] == s2[idx2]:
            sMap[2] += 1
        if answers[i] == s3[idx3]:
            sMap[3] += 1
        
        idx1 += 1
        idx2 += 1
        idx3 += 1
    
    maxV = max(sMap.values())
    maxKey = [key for key, value in sMap.items() if value == maxV]
    
    if sMap[1] == sMap[2] or sMap[2] == [3] or sMap[3] == sMap[1]:
        answer = sorted(maxKey)
    else: 
        answer = [max(sMap, key=sMap.get)]
    
    return answer