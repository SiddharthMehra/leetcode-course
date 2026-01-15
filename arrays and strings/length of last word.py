class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        n = len(s)-1
        length = 0

        while n>=0:

            if s[n]!=" ":
                length+=1
            elif length>0:
                return length
            n-=1
        
        return length
