class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1:
            return True
        arr = []
        while(n!=1):
            arr.append(n)
            num = 0
            while(n):
                a = n%10
                n = n//10
                num+=a*a
            if num in arr:
                return False
            else:
                n = num
        return True