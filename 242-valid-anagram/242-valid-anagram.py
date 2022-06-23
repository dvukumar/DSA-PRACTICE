class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def Tolist(s):
            dict = {}
            n = len(s)
            for i in range(n):
                char = s[i]
                if char in dict:
                    dict[char]+=1
                else:
                    dict[char] = 1
            return dict
        
        dict1 = Tolist(s)
        dict2 = Tolist(t)
        
        return dict1==dict2
        