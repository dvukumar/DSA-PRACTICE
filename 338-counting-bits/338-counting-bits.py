class Solution:
    def countBits(self, n: int) -> List[int]:
        if n==0:
            return [0]
        arr = [0 for _ in range(n+1)]
        arr[0] = 0
        arr[1] = 1
        
        for i in range(2,n+1):
            arr[i] = arr[i//2]+i%2
        return arr