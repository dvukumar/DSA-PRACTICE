class Solution:
    def validPalindrome(self, s: str) -> bool:
        def Palindrome(s):
            l = len(s)-1
            f = 0
            

            while(f<=l):
                if s[f]==s[l]:
                    f+=1
                    l-=1
                else:
                    return False
            return True
        
        f = 0
        l = len(s)-1
        while(f<=l):
            if s[f]==s[l]:
                f+=1
                l-=1
            else:
                s0 = s[f:l]
                s1 = s[f+1:l+1]
                return Palindrome(s0)or Palindrome(s1)
        return True
            
        
         