class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        arr = []
        for point in points:
            x = point[0]
            y = point[1]
            distance = x*x+y*y
            arr.append([distance,point])
        
        arr.sort(key=lambda x:x[0])
        res = []
        for i in range(k):
            val = arr[i][1]
            res.append(val)
        return res