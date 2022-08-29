class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n,m = len(grid),len(grid[0])
        
        def island(grid,i,j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]=="0":
                return 1
            grid[i][j] = "0"
            left = island(grid,i,j-1)
            right = island(grid,i,j+1)
            up = island(grid,i-1,j)
            down = island(grid,i+1,j)
            
            if left and right and up and down:
                
                return True
        
        count = 0
        #print(n,m)
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1":
                    count+=1
                    island(grid,i,j)
        #print(grid)
        return count