def merge(nums1, m, nums2, n):
    answer = sorted(nums1 + nums2)
    
    while(0 in answer):
        answer.remove(0)
    
    return answer

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3 
n = 3

print(merge(nums1, m, nums2, n))



