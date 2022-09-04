class Solution:
    def reverseWords(self, s: str) -> str:
        
        arr = []
        
        word = ""
        i = 0
        while(i<len(s)):
            if len(word)==0 and s[i]==" ":
                i+=1
            elif s[i]==" ":
                arr.append(word)
                word = ""
                i+=1
            else:
                word+=s[i]
                i+=1
        
        if len(word)>0:
            arr.append(word)
            
        arr.reverse()
        res = ""
        for word in arr:
            res+=word+" "
        
        return res[:-1]