class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return nums[0]
        start = 0
        end = len(nums)-1
        
        target = nums[-1]
        
        while(start<=end):
            
            mid = (start+end)//2
            if nums[mid]>target:
                start = mid+1
                smallest = target
            else:
                end = mid-1
                
                target = nums[mid]
                smallest = nums[mid]
        return smallest
                