class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        nums.sort()
        def sumDigit(n):
            sum_ = 0
            while(n):
                sum_+=n%10
                n=n//10
            return sum_
        
        def sumValues(arr):
            
            if len(arr)<2:
                return -1
            if len(arr)>2:
                
                return arr[-1]+arr[-2]
            
            return arr[0]+arr[1]
        
        dict = {}
        count = 0
        for val in nums:
            key = sumDigit(val)
            if key in dict:
                count+=1
                dict[key].append(val)
            else:
                dict[key] = [val]
        
        values = list(dict.values())
        print(dict)
        print(values)
        max_ = 0
        for i in range(len(values)):
            res = sumValues(values[i])
            max_ = max(max_,res)
        if max_==0:
            return -1
        return max_