class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def palindrome(s):
            n = len(s)
            l,r = 0,n-1
            
            while(l<r):
                left = s[l]
                right = s[r]
                if left!=right:
                    return False
                else:
                    l+=1
                    r-=1
            return True
        
        string = ""
        for char in s.lower():
            alpha = ord(char) - ord('a')
            digit = ord(char) - ord('0')
            
            if (alpha<26 and alpha>=0):
                string = string+ char
                
            elif (digit<10 and digit>=0):
                string+=char
        
        return palindrome(string)
                
                