class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        dict = {}
        for num in nums:
            if num in dict:
                dict[num]+=1
            else:
                dict[num] = 1
        
        max1 = max(dict.values())
        temp = {}
        for i in range(len(nums)):
            if nums[i] not in temp and dict[nums[i]]==max1:
                temp[nums[i]] = [i]
            elif nums[i] in temp and dict[nums[i]]==max1:
                temp[nums[i]].append(i)
        
        min1 = 100000
        keys = list(temp.keys())
        for key in keys:
            arr = temp[key]
            len1 = arr[-1] - arr[0]
            if len1<min1:
                min1 = len1+1
        return min1
                