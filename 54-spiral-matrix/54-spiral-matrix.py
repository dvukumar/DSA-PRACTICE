class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row_beg = 0
        row_end = len(matrix)-1
        
        col_beg = 0
        col_end = len(matrix[0])-1
        
        arr = []
        
        while(row_beg<=row_end and col_beg<=col_end):
            
            for i in range(col_beg,col_end+1):
                arr.append(matrix[row_beg][i])
            row_beg+=1
            
            for i in range(row_beg,row_end+1):
                arr.append(matrix[i][col_end])
            col_end-=1
            
            for i in range(col_end,col_beg-1,-1):
                arr.append(matrix[row_end][i])
            row_end-=1
            
            for i in range(row_end,row_beg-1,-1):
                arr.append(matrix[i][col_beg])
            col_beg+=1
        
        print(arr)
        return arr[0:len(matrix)*len(matrix[0])]