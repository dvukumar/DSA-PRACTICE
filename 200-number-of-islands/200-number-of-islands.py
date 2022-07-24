class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row,col,grid):
            if row<0 or col<0 or row>=len(grid) or col>=len(grid[0]):
                return
            if grid[row][col]=="0":
                return
            grid[row][col] = "0"
            dfs(row+1,col,grid)
            dfs(row-1,col,grid)
            dfs(row,col+1,grid)
            dfs(row,col-1,grid)
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    count+=1
                    dfs(i,j,grid)
        
        return count