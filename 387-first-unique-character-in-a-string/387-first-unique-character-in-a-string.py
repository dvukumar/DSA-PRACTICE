class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        dict = {}
        arr = []
        
        for i in range(len(s)):
            char = s[i]
            if char in dict:
                dict[char].append(i)
            else:
                dict[char] = [i]
        
        values = list(dict.values())
        
        for arr in values:
            if len(arr)==1:
                return arr[0]
        return -1
               
            
            