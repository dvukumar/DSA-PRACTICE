class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        if n==1 or (n,k)==(2,1):
            return 0
        
        if k<=(2**(n-1))/2:
            return self.kthGrammar(n-1,k)
        return int(not bool(self.kthGrammar(n,k-(2**(n-1))/2)))
        