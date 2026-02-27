class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        
        n = len(palindrome)
        for i in range(n//2):
            #just replace ith character with a for smallest lexicographical string
            if palindrome[i]!='a':
                return palindrome[:i] + 'a' + palindrome[i+1:]
        
        return palindrome[:-1] + 'b' if n>1 else ""
