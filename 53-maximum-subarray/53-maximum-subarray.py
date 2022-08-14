class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_ = nums[0]
        res = max_
        
        for i in range(1,len(nums)):
            max_ = max(nums[i],nums[i]+max_)
            res = max(res,max_)
        return res