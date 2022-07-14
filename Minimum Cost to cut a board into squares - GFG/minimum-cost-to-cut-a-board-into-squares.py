from typing import List


class Solution:
    def minimumCostOfBreaking(self,X : List[int], Y : List[int],M : int, N : int) -> int:
        
        X.sort(reverse = True)
        Y.sort(reverse = True)
        
        x_piece = 1
        y_piece = 1
        
        i,j = 0,0
        total_cost = 0
        
        while(i<M and j<N):
            
            if X[i]>Y[j]:
                
                total_cost+=X[i]*y_piece
                x_piece+=1
                i+=1
            else:
                
                total_cost+=Y[j]*x_piece
                y_piece+=1
                j+=1
        
        
        while(i<M):
            
            total_cost+=X[i]*y_piece
            x_piece+=1
            i+=1
            
        while(j<N):
            
            total_cost+=Y[j]*x_piece
            y_piece+=1
            j+=1
            
        return total_cost
        
                
        
        


#{ 
#  Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        m = a[0]
        n = a[1]
        
        tmp=IntArray().Input(a[0]-1) + IntArray().Input(a[1]-1)
        X = tmp[:m-1]
        Y = tmp[m-1:]
        
        obj = Solution()
        res = obj.minimumCostOfBreaking(X, Y,m-1,n-1)
        
        print(res)
        

# } Driver Code Ends