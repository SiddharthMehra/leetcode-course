class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = [-1]*128
        left = 0
        max_length = 0

        for right, char in enumerate(s):
            ascii_index = ord(char)

            if last_seen[ascii_index]>=left:
                left = last_seen[ascii_index]+1
            
            last_seen[ascii_index] = right

            max_length = max(max_length, right-left+1)
        
        return max_length
