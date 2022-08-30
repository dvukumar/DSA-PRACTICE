class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        if n==1:
            return 1
        i = 1
        while(n>=i):
            n = n-i
            i+=1
        return i-1