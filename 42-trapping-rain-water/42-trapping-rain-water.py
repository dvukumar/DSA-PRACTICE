class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        maxl = [0]*n
        maxh1 = height[0]
        for i in range(n):
            maxh1 = max(maxh1,height[i])
            maxl[i] = maxh1
        
        maxr = [0]*n
        maxh2 = height[-1]
        for i in reversed(range(n)):
            maxh2 = max(maxh2,height[i])
            maxr[i] = maxh2
            
        StoredWater = 0
        for i in range(n):
            StoredWater+=min(maxl[i],maxr[i])-height[i]
        return StoredWater
        