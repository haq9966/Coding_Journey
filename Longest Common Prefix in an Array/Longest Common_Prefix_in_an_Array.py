#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr, n):
        # code here
        result=""
        arr.sort()
        for i in range(len(arr[0])):
            if arr[0][i]==arr[-1][i]:
                result+=arr[0][i]
            else:
                break
        if result == "":
            return(-1)
        else:
            return result
                
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends
