class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        
        
        arr = [nums[0]]
        max_ = nums[0]
        for i in range(1,len(nums)):
            max_ = max(nums[i],nums[i]+max_,)
            arr.append(max_)
            print(max_)
        return max(arr)