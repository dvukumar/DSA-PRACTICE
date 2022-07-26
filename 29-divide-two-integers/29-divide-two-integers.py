class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend ==0:
            return 0
        if (dividend>0 and divisor>0) or (dividend<0 and divisor<0):
            flag = True
        else:
            flag = False
            
        res = abs(dividend)//abs(divisor)
        if not flag:
            res = res*-1
        if res>2**31-1:
            return 2**31-1
        elif res<-2**31:
            return -2**31
        else:
            return res