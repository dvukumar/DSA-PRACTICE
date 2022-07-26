class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        if len(nums)<3:
            return list(set(nums))
        n = len(nums)/3
        dict = {}
        arr = []
        for i in nums:
            if i in dict:
                dict[i]+=1
            else:
                dict[i] = 1
                
            if dict[i]>n and i not in arr:
                    arr.append(i)
                    
        return arr
                