class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        n = len(candidates)
        result = []
        
        def find_combs(target,temp,ind):
            
            if target==0:
                
                result.append(list(temp))
                return
                return False
            if ind==n or target<0:
                return
            prev = 0
            for i in range(ind,len(candidates)):
                if candidates[i]==prev:
                    continue
                
                temp.append(candidates[i])
                find_combs(target-candidates[i],temp,i+1)
                temp.pop()
                prev = candidates[i]
            
        
        find_combs(target,[],0)
        return result