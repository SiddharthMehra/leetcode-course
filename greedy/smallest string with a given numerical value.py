class Solution:
    def getSmallestString(self, n: int, k: int) -> str:

        ans = ['a']*n
        k-=n #atleast a of ord(1) for each character

        #start from right to left
        while k>0:
            n-=1
            ans[n] = chr(ord('a') + min(25, k))
            k-=min(25, k)
        
        return ''.join(ans)
