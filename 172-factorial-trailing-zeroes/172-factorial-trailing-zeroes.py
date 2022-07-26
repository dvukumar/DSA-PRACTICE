class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        result = 0
    
        arr = [5,25,125,625,3125]
        for i in arr:
            result+=n//i
        return result
        