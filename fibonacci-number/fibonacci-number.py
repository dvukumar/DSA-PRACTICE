class Solution:
    def fib(self, n: int) -> int:
        
        dict = {}
        def f(n):
            if n in dict:
                result = dict[n]
            if n<=1:
                result = n
            else:
                result = f(n-1)+f(n-2)
            
            dict[n] = result
            
            return result
            
        return f(n)