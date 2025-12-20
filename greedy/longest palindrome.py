class Solution:
    def longestPalindrome(self, s: str) -> int:
        character_set = set()
        res = 0
        for c in s:
            if c in character_set:
                #match found
                character_set.remove(c)
                # add two occurences to the palindrome
                res+=2
            else:
                character_set.add(c)
        
        #pick any 1 unmatched character as the middle
        if character_set:
            res+=1
        
        return res
            
        
            
        
