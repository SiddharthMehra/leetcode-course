class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        n, m = len(haystack), len(needle)
        if m>n:
            return -1
        
        base = 31
        MOD = 10**9+7

        power = 1
        for _ in range(m-1):
            power = (power*base) % MOD
        
        needle_hash, window_hash = 0, 0
        for i in range(m):
            needle_hash = (needle_hash * base + ord(needle[i])) % MOD
            window_hash = (window_hash * base + ord(haystack[i])) % MOD
        
        #compare first window
        if window_hash == needle_hash and haystack[:m] == needle:
            return 0
        
        #slide the window, remove left char and add right char

        for i in range(m, n):
            window_hash = (window_hash - ord(haystack[i-m]) * power) % MOD
            window_hash = (window_hash * base + ord(haystack[i])) % MOD
        
            start = i-m+1
            if window_hash == needle_hash:
                if haystack[start:start+m] == needle:
                    return start
            
        
        return -1
            
