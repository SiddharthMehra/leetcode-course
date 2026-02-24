class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:

        zeros, seconds = 0, 0
        for c in s:
            if c == '0':
                zeros+=1
            elif zeros>0:
                seconds = max(seconds+1, zeros)
        
        return seconds
