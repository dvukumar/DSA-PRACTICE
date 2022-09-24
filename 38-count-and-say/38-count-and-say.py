class Solution:
    def countAndSay(self, n: int) -> str:
        
        def helper(s):
            res = ""
            count = 0
            for i in range(len(s)):
                if i==0:
                    val = s[i]
                    count+=1
                elif s[i]==val:
                    count+=1
                else:
                    res+=str(count)+val
                    count = 1
                    val = s[i]
            res+=str(count)+val
            return res
        
        
        for i in range(1,n+1):
            if i==1:
                res = "1"
            else:
                res = helper(res)
        return res
            
            