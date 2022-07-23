class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def BinarySearch(arr,val):
            l = 0
            r = len(arr)-1
            
            while(l<=r):
                mid = (l+r)//2
                if arr[mid]==val:
                    while(True):
                        if mid>0 and arr[mid-1]==val:
                            
                            mid = mid-1
                        else:
                            break
                    return mid
                elif arr[mid]>val:
                    r = mid-1
                else:
                    l = mid+1
            return -1
        arr = [_ for _ in nums]
        arr.sort()
        print(arr)
        res = []
        for num in nums:
            i = BinarySearch(arr,num)
            res.append(i)
            arr.pop(i)
        return res
    
        