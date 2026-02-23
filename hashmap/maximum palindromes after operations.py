class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:

        count = Counter(c for w in words for c in w)
        A = sorted(map(len, words))
        pairs = sum(v//2 for v in count.values())

        # we need a//2 to form palindrome
        for i,a in enumerate(A):
            pairs-=a//2
            if pairs<0:
                return i
        
        return len(A)
        
