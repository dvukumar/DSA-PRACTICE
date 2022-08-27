class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        
        def counter(n,dict):
            while(n):
                c = n%10
                n = n//10
                if c in dict:
                    dict[c]+=1
                else:
                    dict[c] = 1
            return dict
        
        count = counter(n,{})
        
        for i in range(0,31):
            num = 1<<i
            d = counter(num,{})
            if d==count:
                return True
        return False