class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        def freq(s,dict):
            
            for char in s:
                if char in dict:
                    dict[char]+=1
                else:
                    dict[char] = 1
            return dict
        
        dict1 = freq(ransomNote,{})
        dict2 = freq(magazine,{})
        
        keys = list(dict1.keys())
        
        for key in keys:
            if key not in dict2:
                return False
            if dict1[key]>dict2[key]:
                return False
        return True