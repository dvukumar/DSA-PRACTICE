class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        n = len(columnTitle)
        num = 0
        i = 0
        for char in columnTitle:
            val = ord(char) - ord('A')+1
            num+=val*26**(n-i-1)
            i+=1
        return num