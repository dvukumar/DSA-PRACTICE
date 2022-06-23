class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in range(len(nums1)):
            a = nums1[i]
            nums2.append(a)
        nums2.sort()
        n = len(nums2)
        if (n%2!=0):
            i = n//2
            return nums2[i]
        else:
            i1 = n//2
            i2 = n//2 - 1
            return (nums2[i1]+nums2[i2])/2
            