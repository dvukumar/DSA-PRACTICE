class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def palindrome(s,count,i,j):
            if count>1:
                return False
            if i>=j:
                return True
            if s[i]==s[j]:
                return palindrome(s,count,i+1,j-1)
            else:
                return palindrome(s,count+1,i+1,j) or palindrome(s,count+1,i,j-1)
        
        res = palindrome(s,0,0,len(s)-1)
        return res