class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        dict = {}
        arr = []
        
        for i in range(len(s)):
            val = s[i]
            if val in dict:
                dict.pop(val)
                arr.append(val)
            else:
                if val not in arr:
                    dict[val] = 1
        
        keys = list(dict.keys())
        if len(keys)==0:
            return -1
        key = keys[0]
        
        for i in range(len(s)):
            val = s[i]
            if val==key:
                return i
        return -1
            
        