class Solution:
    def equalFrequency(self, word: str) -> bool:

        char_count = Counter(word)

        #try removing one occurence of each letter
        for ch in list(char_count.keys()):
            char_count[ch]-=1

            if char_count[ch] == 0:
                del char_count[ch]

            if len(set(char_count.values())) == 1:
                return True
            
            char_count[ch] = char_count.get(ch, 0) + 1
        
        return False
        
