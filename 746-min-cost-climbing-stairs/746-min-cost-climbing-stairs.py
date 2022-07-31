class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        arr = [0 for _ in range(len(cost))]
        
        arr[0] = cost[0]
        arr[1] = cost[1]
        
        for i in range(2,len(cost)):
            arr[i] = min(cost[i]+arr[i-1],cost[i]+arr[i-2])
        return arr[-1]