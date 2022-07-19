class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        arr = [[1 for _ in range(i)] for i in range(1,numRows+1)]
        
        for i in range(2,numRows):
            for j in range(1,i):
                arr[i][j] = arr[i-1][j-1]+arr[i-1][j]
        return arr