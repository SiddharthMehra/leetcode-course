class Solution:
    def repeatedCharacter(self, s: str) -> str:
        total = set()

        for ch in s:

            if ch in total:
                return ch
            else:
                total.add(ch)
