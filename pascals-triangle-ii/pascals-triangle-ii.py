class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        
        
        
        j = 2
        arr = [1,1]
        while(j<=rowIndex):
            
            n_arr = [1]
            i = 1
            while(i<=j-1):
                n = arr[i]+arr[i-1]
                n_arr.append(n)
                i+=1
            n_arr.append(1)
            arr = n_arr
            j+=1
        return arr