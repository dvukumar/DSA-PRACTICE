class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        nums.sort()
        dict = {}
        
        for i in nums:
            if i in dict:
                dict[i]+=1
            else:
                dict[i] = 1
                
        # keys = list(dict.keys())
        # values = list(dict.values())
        arr = []
        for _ in range(k):
            maxkey = max(zip(dict.values(),dict.keys()))[1]
            arr.append(maxkey)
            del dict[maxkey]
        
        return arr