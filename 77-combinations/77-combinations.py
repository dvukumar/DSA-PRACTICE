class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        
        def backtracking(i,arr):
            
            if i>n+1:
                return
            if len(arr)==k:
                res.append(list(arr))
                return
            
            for j in range(i,n+1):
                arr.append(j)
                backtracking(j+1,arr)
                arr.pop()
        backtracking(1,[])
        return res