class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            arr = []
            a = nums[i]
            nums.pop(i)
            temp = target-a
            if temp in nums:
                arr.append(i)
                j = nums.index(temp)
                arr.append(j+1)
                return arr
            else:
                nums.insert(i,a)