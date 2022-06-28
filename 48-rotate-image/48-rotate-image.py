class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        
        arr = []
        
        for j in range(m):
            arr0 = []
            for i in range(n):
                val = matrix[i][j]
                arr0.append(val)
            arr0.reverse()
            arr.append(arr0)
        
        for i in range(n):
            for j in range(n):
                val = arr[i][j]
                matrix[i][j] = val
        print(matrix)
                