class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans, prev, curr = 0, 0, 1
        for i in range(1, len(s)):
            #run ended, curr initialised to 1 for new block, prev = curr
            if s[i-1]!=s[i]:
                ans+=min(prev, curr)
                prev, curr = curr, 1
            else:
                #continue the streak
                curr+=1
        return ans + min(prev, curr)

        
