class Solution:
    def countPrimes(self, n: int) -> int:
        
        arr = [1 for _ in range(n)]
        if n<2:
            return 0
        for i in range(2,n):
            if i*i>=n:
                break
            
            if arr[i] == 1:
                for j in range(i*i,n,i):
                    arr[j] = 0
        count = 0
        
        for j in arr:
            if j==1:
                count+=1
        return count-2