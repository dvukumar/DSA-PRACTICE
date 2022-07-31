class NumArray:
    arr = []
    s = 0
    l = 0
    def __init__(self, nums: List[int]):
        self.arr = nums
        self.s = sum(nums)
        self.l = len(nums)
        

    def update(self, index: int, val: int) -> None:
        self.s-=self.arr[index]
        self.arr[index] = val
        self.s+=val

    def sumRange(self, left: int, right: int) -> int:
        if (right-left)>self.l//2:
            ans = sum(self.arr[:left])+sum(self.arr[right+1:])
            return self.s - ans
        ans = sum(self.arr[left:right+1])
        return ans


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)