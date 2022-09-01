class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        i = n-1
        count = 0
        while(i>0):
            
            for j in range(i-1,-1,-1):
                if j + nums[j]>=i:
                    ind = j
            i = ind
            count+=1
        return count
                