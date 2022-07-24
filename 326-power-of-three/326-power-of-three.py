class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==0:
            return False
        if n==1:
            return True
        while(n):
            if n%3==0 or n==1:
                n=n//3
            else:
                return False
        return True
            