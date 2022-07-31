class Solution:
    def divisorGame(self, n: int) -> bool:
        count = 0
        while(n>1):
            for x in range(1,n):
                if(n%x==0):
                    n = n-x
                    count+=1
                    break
        print(count)
                
        if count%2==0:
            return False
        else:
            return True
                
            