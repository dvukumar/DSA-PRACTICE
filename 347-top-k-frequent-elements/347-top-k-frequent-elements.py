class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        nums.sort()
        dict = {}
        
        for i in nums:
            if i in dict:
                dict[i]+=1
            else:
                dict[i] = 1
                
        arr = []
        for key in dict.keys():
            a = [key,dict[key]]
            arr.append(a)
        
        arr.sort(key = lambda x:x[1])
        arr.reverse()
        res = []
        for i in range(k):
            res.append(arr[i][0])
        return res