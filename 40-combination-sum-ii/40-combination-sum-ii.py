class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        # candidates = [1,1,2,5,6,7,10],target = 8
        result = []
        def backtracking(target,ind,arr):
            
            if ind>len(candidates) or target<0:
                return
            #print(arr,target)
            if target==0:
                if arr not in result:
                    result.append(list(arr))
                return

            prev = 0
            for i in range(ind,len(candidates)):
                curr = candidates[i]
                if curr==prev:
                    continue
                arr.append(curr)
                backtracking(target-curr,i+1,arr)
                arr.pop()
                prev = curr
            return 
        backtracking(target,0,[])
        return result
                