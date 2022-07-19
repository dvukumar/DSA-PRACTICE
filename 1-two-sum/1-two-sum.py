class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        arr = [i for i in nums]
        arr.sort() #O(NlogN)
        dict = {}
        
        for i in range(len(nums)):
            val = nums[i]
            if val in dict:
                dict[val].append(i)
            else:
                dict[val] = [i]
        
        
        for i in range(len(nums)):
            first = nums[i]
            second = target - first
            
            if second in dict:
                
                if first==second:
                    if len(dict[first])>1:
                        idx1 = dict[first][0]
                        idx2 = dict[first][1]
                        break
                else:
                    idx2 = dict[second][0]
                    idx1 = dict[first][0]
                    break

                
                
        
        print(dict)
        return [idx1,idx2]
        