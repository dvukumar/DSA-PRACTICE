class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        res = []
        l = 0
        r = len(nums)-1
        
        while(l<=r):
            mid = (l+r)//2
            if nums[mid]==target:
                if mid>0 and nums[mid-1]==target:
                    r = mid - 1
                else:
                    res.append(mid)
                    break
            elif nums[mid]>target:
                r = mid - 1
            
            else:
                l = mid+1
        
        if len(res)==0:
            res.append(-1)
            
        l = 0
        r = len(nums)-1
        
        while(l<=r):
            mid = (l+r)//2
            if nums[mid]==target:
                if mid<len(nums)-1 and nums[mid+1]==target:
                    l = mid + 1
                else:
                    res.append(mid)
                    break
            elif nums[mid]>target:
                r = mid - 1
            
            else:
                l = mid+1
        
        if len(res)==1:
            res.append(-1)
        return res