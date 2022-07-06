class Solution:
    def climbStairs(self, n: int) -> int:
        
        res = {}
        def climb(n):
            if n in res:
                result = res[n]
            elif n<=2:
                result = n
            else:
                result = climb(n-1)+climb(n-2)
            
            res[n] = result
            
            return result
        
        return climb(n)