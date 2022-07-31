class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def Count(num,count):
            
            while(num):
                if num%2==1:
                    count+=1
                num = num//2
            return count
        
        arr = [0 for _ in range(n+1)]
        
        for i in range(n+1):
            c = Count(i,0)
            arr[i] = c
        return arr
                