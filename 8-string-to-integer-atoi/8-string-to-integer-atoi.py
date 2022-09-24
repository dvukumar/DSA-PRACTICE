class Solution:
    def myAtoi(self, s: str) -> int:
       
        s = s.strip()
      
        res = []
        if len(s)==0:
            return 0
        if s[0]=='+' or s[0]=='-' or s[0]=='.' or s[0].isnumeric():
            res.append(s[0])
        else:
            
            return 0
        
        for i in range(1,len(s)):
            
            if s[i].isnumeric() or (s[i]=='.' and s[i] not in res):
                res.append(s[i])
            else:
                break
        
        resStr = "".join(res)
        if len(resStr)==1 and (resStr[0] in ['+','-','.']):
            return 0
        num = int(float(resStr))
        # print(resStr,num)
        if num<=2**31-1 and num>=-2**31:
            return num
        if num>0:
            return 2**31-1
        else:
            return -2**31