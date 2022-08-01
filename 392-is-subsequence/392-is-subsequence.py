class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s)>len(t):
            return False
        
        while(t and s):
            s0 = s[0]
            t0 = t[0]
            
            if s0==t0:
                s = s[1:]
            t = t[1:]
        return len(s)==0