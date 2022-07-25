class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def findIndex(arr,target):
            l = 0
            r = len(arr)-1
            res = []
            check = []
            while(l<=r):
                mid = (l+r)//2
                
                if arr[mid]==target:
                    check.append(mid)
                    r = mid-1
                elif arr[mid]>target:
                    r = mid-1
                else:
                    l = mid+1
            if len(check)==0:
                res.append(-1)
            else:
                minInd = min(check)
                res.append(minInd)   
            check.clear()
            l = 0
            r = len(arr)-1
            while(l<=r):
                mid = (l+r)//2
                if arr[mid]==target:
                    check.append(mid)
                    l = mid+1
                elif arr[mid]>target:
                    r = mid-1
                else:
                    l = mid+1
            if len(check)==0:
                res.append(-1)
            else:
                maxInd = max(check)
                res.append(maxInd)   
            
            return res
        return findIndex(nums,target)