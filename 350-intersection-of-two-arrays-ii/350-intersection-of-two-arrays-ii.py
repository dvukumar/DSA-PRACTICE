class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        arr = []
        for num in nums1:
            if len(nums2)==0:
                break
            if num in nums2:
                arr.append(num)
                nums2.remove(num)
        return arr
                