class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []
        def dp(openP,closeP):
            if openP==closeP==n:
                res = "".join(stack)
                result.append(res)
                return
            
            if openP<n:
                stack.append('(')
                dp(openP+1,closeP)
                stack.pop()
            if closeP<openP:
                stack.append(')')
                dp(openP,closeP+1)
                stack.pop()
        dp(0,0)
        return result

        