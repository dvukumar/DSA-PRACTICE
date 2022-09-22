class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        m,n = len(grid),len(grid[0])
        
        def isTrue(row,col):
            if row<0 or row>=m:
                return False
            if col<0 or col>=n:
                return False
            return True
        
        dict = {}
        def isIsland(row,col):
            
            if (row,col) in dict:
                return 0
            if isTrue(row,col)==False:
                return 0
            
            if grid[row][col]==0:
                return 0
            dict[(row,col)] = 1
            
            left = isIsland(row,col-1)
            right = isIsland(row,col+1)
            up = isIsland(row-1,col)
            down =isIsland(row+1,col)
            
            return 1+left+right+up+down
        
        maxArea = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    continue
                area = isIsland(i,j)
                maxArea = max(maxArea,area)
        return maxArea