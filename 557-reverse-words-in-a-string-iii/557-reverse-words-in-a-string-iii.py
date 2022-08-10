class Solution:
    def reverseWords(self, s: str) -> str:
        
        def reverse(string):
            s0 = ""
            for i in string:
                s0 = i+s0
            return s0
            
        string = ""
        res = ""
        for char in s:
            if char ==" ":
                
                res+=reverse(string)
                res = res+" "
                string = ""
            else:
                string+=char
                
        res+=reverse(string)
        return res