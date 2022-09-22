class Solution:
    def reverseWords(self, s: str) -> str:
              
        string = ""
        res = ""
        for char in s:
            if char ==" ":
                
                res+=string[::-1]
                res = res+" "
                string = ""
            else:
                string+=char
                
        res+=string[::-1]
        return res