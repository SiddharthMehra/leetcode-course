class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:

        def devowel(word):
            word = word.lower()
            return "".join('*' if c in 'aeiou' else c for c in word)
        
        words_perfect = set(wordlist)
        words_cap = {}
        words_vow = {}

        for word in wordlist:
            wl = word.lower()
            words_cap.setdefault(wl, word)
            words_vow.setdefault(devowel(wl), word)
        
        def solve(query):
            if query in words_perfect:
                return query
            
            ql = query.lower()
            if ql in words_cap:
                return words_cap[ql]
            
            qv = devowel(ql)
            if qv in words_vow:
                return words_vow[qv]
            
            return ""
        
        return [solve(q) for q in queries]
