#User function Template for python3
class Solution:

	def findSum(self,a, b):
		# code here
		str1 = ""
		str2 = ""
		
		i = 0
		while(i<len(a)):
		    val = a[i]
		    str1+=str(val)
		    i+=1
		
		i = 0
		while(i<len(b)):
		    val = b[i]
		    str2+=str(val)
		    i+=1
		
		sum = int(str1)+int(str2)
		sum = str(sum)
		n = len(sum)
		arr = []
		i = 0
		while(i<n):
		    val = sum[i]
		    arr.append(int(val))
		    i+=1
		
		return arr
		    

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findSum(a, b)
        for i in ans:
            print(i, end=" ")
        print()
        tc -= 1

# } Driver Code Ends