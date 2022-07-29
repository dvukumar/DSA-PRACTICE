class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums)
        list = [0]*len(nums)
        list[0] = nums[0]
        list[1] = max(nums[0],nums[1])
        
        for i in range(2,len(nums)):
            list[i] = max((nums[i]+list[i-2]),list[i-1])
            
        return list[-1]