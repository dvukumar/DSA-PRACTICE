class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        j = len(nums)-1
        prevs = -1
        prevl = len(nums)+1
        while(i<=j):
            if nums[i]+nums[j]==len(nums):
                prevs = nums[i]
                prevl = nums[j]
                i+=1
                j-=1
                
            else:
                if nums[i]+nums[j]<len(nums):
                    return prevl-1
                else:
                    return prevs+1
        return prevs+1
        