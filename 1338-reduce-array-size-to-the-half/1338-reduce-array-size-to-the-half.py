class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        length = len(arr)
        dict = {}
        for num in arr:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        
        
        val = list(dict.values())
        val.sort()
        val.reverse()
        
        count = 0
        n = length
        for value in val:
            
            n = n-value
            count+=1
            if n<=length//2:
                return count
        return -1
            
        
        
            