class Solution:
    def partitionString(self, s: str) -> int:
        lastSeen = [-1]*26
        count = 1
        substringStart = 0

        for i in range(len(s)):
            #char already exists in the substring
            if lastSeen[ord(s[i]) - ord('a')]>=substringStart:
                count+=1
                substringStart = i
            lastSeen[ord(s[i]) - ord('a')] = i
        
        return count
