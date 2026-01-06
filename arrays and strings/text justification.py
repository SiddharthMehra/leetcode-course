class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, curr, num_of_letters = [], [], 0
        for w in words:
            #number of letters currently + number of letters in this word + number of spaces required for curr+1 words
            if num_of_letters + len(w) + len(curr)>maxWidth:
                #insert spaces in round robin fashion. if only 1 word 1 space
                for i in range(maxWidth - num_of_letters):
                    curr[i%(len(curr)-1 or 1)] +=' '
                res.append(''.join(curr))
                curr, num_of_letters = [], 0
            
            curr+=[w]
            num_of_letters+=len(w)
        
        #just left adjust the last line
        return res + [' '.join(curr).ljust(maxWidth)]


