class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0,n-1
        if n==1:
            return 0
        while(l<=r):
            mid = (l+r)//2
            
            if mid==0:
                if nums[mid+1]<nums[mid]:
                    return mid
                else:
                    l = mid+1
            elif mid==n-1:
                if nums[mid]>nums[mid-1]:
                    return mid
                else:
                    r = mid-1
            elif nums[mid]>nums[mid-1]:
                if nums[mid]>nums[mid+1]:
                    return mid
                else:
                    l = mid+1
            elif nums[mid]<nums[mid+1]:
                if nums[mid]<nums[mid-1]:
                    l = mid+1
                
            elif nums[mid]>nums[mid+1]:
                if nums[mid]<nums[mid-1]:
                    r = mid-1
                else:
                    return mid
                
            
                