class Solution:
    
    def climbStairs(self, n: int) -> int:
        res = {}
        def Stairs(n):
            if n in res:
                result = res[n]
            elif n<=2:
                result = n
            else:
                result = Stairs(n-1)+Stairs(n-2)
                res[n] = result
            return result
        return Stairs(n)