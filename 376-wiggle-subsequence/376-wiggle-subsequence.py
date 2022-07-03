class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        
        f = 1
        d = 1
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]>0:
                f = d+1
            if nums[i]-nums[i-1]<0:
                d = f+1
        return max(f,d)
            