class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_ = nums[0]
        min_ = nums[0]
        res = nums[0]
        
        for i in range(1,len(nums)):
            curr = nums[i]
            temp = max(max_*curr,min_*curr,curr)
            min_ = min(max_*curr,min_*curr,curr)
            max_ = temp
            
            res = max(max_,res)
        return res