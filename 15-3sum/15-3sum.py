class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = []
        nums.sort()
        print(nums)
        for i in range(len(nums)):
            if i>0 and nums[i-1]==nums[i]:
                continue
            
            left = i+1
            right = len(nums)-1
            
            while(left<right):
                currSum = nums[i]+nums[left]+nums[right]
                #print(currSum)
                if currSum==0:
                    arr.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    
                    while(left<right and nums[left-1]==nums[left]):
                        left+=1
                    while(right>left and nums[right+1]==nums[right]):
                        right-=1
                elif currSum>0:
                    right-=1
                else:
                    left+=1
        return arr

                    