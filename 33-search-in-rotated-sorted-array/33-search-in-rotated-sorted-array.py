class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s = 0
        l = len(nums)-1
        
        
        while(s<=l):
            mid = (s+l)//2
            if nums[mid]==target:
                return mid
            
            if nums[mid]>=nums[s]:
                if target<nums[mid]:
                    if target <nums[s]:
                        s = mid+1
                    else:
                        l = mid-1
                else:
                    s = mid+1
            else:
                if target>nums[mid]:
                    if target>nums[l]:
                        l = mid-1
                    else:
                        s = mid+1
                else:
                    l = mid-1
        return -1