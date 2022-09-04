class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        dict = {}
        for num in nums:
            if num in dict:
                dict[num]+=1
            else:
                dict[num] = 1
                
        keys = list(dict.keys())
        
        for key in keys:
            if dict[key]==1:
                return key