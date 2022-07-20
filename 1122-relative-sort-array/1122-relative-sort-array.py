class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dict = {}
        for i in arr1:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        arr = []
        for i in arr2:
            count = dict[i]
            while(count):
                arr.append(i)
                count-=1
            del dict[i]
        
        keys = list(dict.keys())
        values = list(dict.values())
        keys.sort()
        for key in keys:
            count = dict[key]
            while(count):
                arr.append(key)
                count-=1
        return arr
                