class Solution:
    def convert(self, s: str, n: int) -> str:
        if n==1:
            return s
        rows = [[] for i in range (n)]
        curr_row = 0
        increment = 1
        i = 0
        result = ''
        while(i<len(s)):
            if curr_row==0:
                increment = 1
            elif curr_row==n-1:
                increment = -1
            
            rows[curr_row].append(s[i])
            curr_row+=increment
            i+=1
            
        for i in rows:
            result+=''.join(i)
        return result
            
        