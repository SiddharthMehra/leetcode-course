class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        first, longest_prefix = 0, 0
        while first<len(s) and longest_prefix<len(t):
            if s[first] == t[longest_prefix]:
                longest_prefix+=1
            first+=1
        
        #remaining characters to be appended to t is the difference in subsequence
        return len(t) - longest_prefix
