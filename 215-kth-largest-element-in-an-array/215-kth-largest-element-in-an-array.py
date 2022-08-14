import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        arr = []
        for i in nums:
            if len(arr)<k:
                heapq.heappush(arr,i)
            else:
                if arr[0]<i:
                    heapq.heappush(arr,i)
                    #print(arr)
                    heapq.heappop(arr)
        return arr[0]
        