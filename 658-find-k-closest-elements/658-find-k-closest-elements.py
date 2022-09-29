class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        import heapq
        heap = []
        heapq.heapify(heap)
        for i in range(k):
            heappush(heap,arr[i])
        
        for i in range(k,len(arr)):
            if abs(arr[i]-x)<abs(heap[0]-x):
                heappop(heap)
                heappush(heap,arr[i])
        
        heap.sort()
        return heap