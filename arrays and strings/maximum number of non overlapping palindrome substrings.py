class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:

        n, ans, start = len(s), 0, 0
        for centre in range(2 * n - 1):
            #handles both odd and even cases
            left = centre//2
            right = left + centre%2

            while left>=start and right<n and s[left] == s[right]:
                if (right-left+1)>=k:
                    ans+=1
                    start = right+1
                    break
                left-=1
                right+=1

        return ans
            
