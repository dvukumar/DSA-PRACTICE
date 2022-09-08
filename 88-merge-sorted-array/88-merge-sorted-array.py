class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i = 0
        j = 0
        while(j<len(nums2) and i<len(nums1)):
            #print(i,j)
            if nums1[i]<=nums2[j]:
                i+=1
            else:
                val = nums2[j]
                nums1.insert(i,val)
                nums1.pop()
                j+=1
        
        for i in range(1,n-j+1):
            nums1[-1*i] = nums2[-1*i]
        