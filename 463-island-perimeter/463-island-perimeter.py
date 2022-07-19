class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        def perimeter(grid,i,j):
            
            if grid[i][j]==0:
                return 0
            return (i==0 or grid[i-1][j]==0)+(i==len(grid)-1 or grid[i+1][j]==0)+(j==0 or grid[i][j-1]==0)+(j==len(grid[0])-1 or grid[i][j+1]==0)
        
        row,col = len(grid),len(grid[0])
        
        result = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    result+=perimeter(grid,i,j)
                    #print(result)
        return result
        
        