class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def BinarySearch(arr,target):
            l,r = 0,len(arr)-1
            ans = 0
            while(l<=r):
                mid = (l+r)//2
                if arr[mid]==target:
                    return mid
                if arr[mid]>target:
                    ans = mid
                    r = mid-1
                else:
                    
                    l = mid+1
            # if arr[mid]>target and mid>0:
            #     return mid - 1
            return ans
        
        arr = [nums[0]]
        
        for i in range(1,len(nums)):
            if nums[i]>arr[-1]:
                arr.append(nums[i])
            else:
                j = BinarySearch(arr,nums[i])
                arr[j] = nums[i]
            #print(arr)
        return len(arr)