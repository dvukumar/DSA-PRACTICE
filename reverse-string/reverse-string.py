class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        def rev(s,i,n):
            if i==len(s)//2:
                return
            rev(s,i+1,n)
            s[i],s[n-i-1] = s[n-i-1],s[i]
        
        n = len(s)
        rev(s,0,n)
            
        