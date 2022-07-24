class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        num = 0
        for n in digits:
            num = num*10+n
        num = num+1
        arr = []
        while(num):
            d = num%10
            num = num//10
            arr.append(d)
        arr.reverse()
        return arr