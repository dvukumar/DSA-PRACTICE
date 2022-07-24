class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def generate(Open,Close,curr):
            if Open<0 or Close<0 or Close<Open:
                return
            if Open==Close and Open==0:
                result.append("".join(curr))
                return
            generate(Open-1,Close,curr+['('])
            generate(Open,Close-1,curr+[')'])
        generate(n,n,[])
        return result