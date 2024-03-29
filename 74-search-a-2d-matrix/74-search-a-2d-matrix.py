class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m,n = len(matrix),len(matrix[0])
        i,j = m-1,0
        
        while(i>=0 and j<n):
            val = matrix[i][j]
            if val==target:
                return True
            elif val>target:
                i-=1
            else:
                j+=1
                    
        return False