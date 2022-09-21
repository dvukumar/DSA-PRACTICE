class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        # def evenSum(arr):
        #     s = 0
        #     for num in arr:
        #         if num%2==0:
        #             s+=num
        #     return s
        evenSum = 0
        for num in nums:
            if num%2==0:
                evenSum+=num
        
        ans = []
        for query in queries:
            val,idx = query[0],query[1]
            
            if val%2==0:
                if nums[idx]%2==0:
                    evenSum+=val
                    ans.append(evenSum)
                else:
                    ans.append(evenSum)
                nums[idx] += val
            else:
                if nums[idx]%2==0:
                    evenSum-=nums[idx]
                    ans.append(evenSum)
                else:
                    evenSum += val+nums[idx]
                    ans.append(evenSum)
                nums[idx] += val
            
            
        return ans