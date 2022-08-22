class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        flag = True
        if(n%4!=0 and n!=1) or n<=0:
            
            return False
        while(n>1):
            n = n>>2
            #print(n)
            if (n%4!=0 or n==0) and n!=1:
                flag = False
            
        return flag