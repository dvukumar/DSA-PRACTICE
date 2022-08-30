class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        arr = []
        res = []
        def BinarySearch(arr,target):
            l = 0
            r = len(arr)-1
            
            while(l<=r):
                mid = (l+r)//2
                if arr[mid]==target:
                    return mid
                if arr[mid]>target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -10000
        
        for i in range(len(numbers)):
            num = numbers[i]
            # if num>target:
            #     arr.append(num)
            #     continue
            
            n = target - num
            
            j = BinarySearch(arr,n)
            if j==-10000:
                arr.append(num)
            else:
                res.append(j+1)
                res.append(i+1)
                break
        return res
        