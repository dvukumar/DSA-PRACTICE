class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums)==0:
            return 0
        nums.sort()
        n = len(nums)
        arr = []
        count = 1
        i = 0
        while(i<n-1):
            if nums[i+1]-nums[i]==1:
                i+=1
                count+=1
            elif nums[i+1]-nums[i]==0:
                i+=1
            else:
                arr.append(count)
                count = 1
                i+=1
        arr.append(count)
        return max(arr)