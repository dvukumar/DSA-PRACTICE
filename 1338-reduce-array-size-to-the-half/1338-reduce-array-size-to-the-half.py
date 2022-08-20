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
        keys = list(dict.keys())
        array = []
        print(keys)
        for key in keys:
            val = dict[key]
            array.append([key,val])
        
        array.sort(key = lambda x:x[1])
        array.reverse()
        
        count = 0
        n = length
        print(array)
        for l in array:
            value = l[1]
            n = n-value
            count+=1
            if n<=length//2:
                return count
        return -1
            
        
        
            