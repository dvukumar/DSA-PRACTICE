class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        arr = [i for i in nums]
        arr.sort() #O(NlogN)
        
        def BinarySearch(arr,target):
            l = 0
            r = len(arr)-1
            
            while(l<=r):
                mid = (l+r)//2
                if target==arr[mid]:
                    return target
                elif target>arr[mid]:
                    l = mid+1
                else:
                    r = mid-1
            return 10**10
            
        
        for i in range(len(arr)):
            temp = arr.pop()
            
            new = target-temp
            
            find = BinarySearch(arr,new)
            
            if find == 10**10:
                continue
            else:
                break
        print(temp,find)
        idx1 = nums.index(temp)
        nums[idx1] = 10**10
        idx2 = nums.index(find)
        
        if idx1<idx2:
            return [idx1,idx2]
        else:
            return [idx2,idx1]
        
        
            
        