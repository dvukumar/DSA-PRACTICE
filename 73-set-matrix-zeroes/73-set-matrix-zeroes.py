class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def set0(matrix,i,j):
            m = len(matrix)
            n = len(matrix[0])
            for r in range(m):
                for l in range(n):
                    matrix[i][l] = 0
                    matrix[r][j] = 0
                        
        
        m = len(matrix)
        n = len(matrix[0])
        arr = []
        
        for i in range(m):
            for j in range(n):
                val = matrix[i][j]
                if val==0:
                    arr.append([i,j])
        print(arr)
        for i in range(len(arr)):
            r = arr[i][0]
            l = arr[i][1]
            set0(matrix,r,l)
        