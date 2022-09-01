class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
     
        def dp(arr,i):
            if i<0 or i>=len(arr):
                return False
            
            if arr[i]==-1:
                return False
            
            if arr[i]==0:
                return True
           
            
            val = arr[i]
            arr[i] = -1
            
            return(dp(arr,i+val) or dp(arr,i-val))
            
        ans = dp(arr,start)
        
        return ans
        