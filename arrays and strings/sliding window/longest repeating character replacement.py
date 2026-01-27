class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left, map, max_freq = 0, defaultdict(int), 0
        ans = 0
        for right in range(len(s)):
            map[s[right]]+=1

            max_freq = max(max_freq, map[s[right]])

            is_valid = (right-left+1 - max_freq<=k)
            if not is_valid:
                map[s[left]]-=1
                left+=1
            
            ans = (right-left+1)

        return ans            


