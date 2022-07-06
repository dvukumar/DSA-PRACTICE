class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        flag = False
        if n<0:
            n = -1*n
            flag = True
        def pow(x,n):
            if n==0:
                return 1
            elif x==0:
                return 0
            else:
                res = pow(x,n//2)
                
                if n%2==0:
                    return res*res
                else:
                    return res*res*x
        
        res = pow(x,n)
        if flag:
            return 1/res
        else:
            return res