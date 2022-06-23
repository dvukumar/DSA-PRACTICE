class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l = 0
        r = len(height)-1
        MaxWater = 0
        while(l<r):
            left = height[l]
            right = height[r]
            if left<right:
                water = left*(r-l)
                l+=1
            else:
                water = right*(r-l)
                r-=1
            MaxWater =max(MaxWater,water) 
        return MaxWater