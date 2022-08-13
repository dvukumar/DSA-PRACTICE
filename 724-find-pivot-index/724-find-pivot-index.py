class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        arr = [_ for _ in nums]
        n = len(arr)
        for i in range(1,n):
            nums[i] = nums[i-1]+nums[i]
            arr[n-i-1] = arr[n-i] + arr[n-i-1]
        # print(nums)
        # print(arr)
        
        for i in range(len(arr)):
            if nums[i]==arr[i]:
                return i
        return -1