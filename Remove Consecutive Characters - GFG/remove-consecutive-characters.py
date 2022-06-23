#User function Template for python3

class Solution:
    def removeConsecutiveCharacter(self, S):
        # code here
        n = len(S)
        if n==1:
            return S
        l = 0
        r = 1
        for i in range(n-1):
            left = S[l]
            right = S[r]
            if left==right:
                S = S[:l+1]+S[r+1:]
            else:
                l+=1
                r+=1
        return S

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        s = input()
        ob = Solution()
        print(ob.removeConsecutiveCharacter(s))

# } Driver Code Ends