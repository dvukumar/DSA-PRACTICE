class Solution:
    def longestPalindrome(self, s: str) -> str:
        string = ""
        
        def palindrom(left,right,s):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return s[left+1:right]
            
            
        for i in range(len(s)):
            temp = palindrom(i,i,s)
            if len(temp)>len(string):
                string = temp
                
            res = palindrom(i,i+1,s)
            if len(res)>len(string):
                string = res
        return string