class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = i = 0
        res = []

        for j, v in enumerate(s):
            count = count+1 if v == '1' else count-1
            #balanced string
            if count == 0:
                #recursive
                res.append('1' + self.makeLargestSpecial(s[i+1: j]) + '0')
                i = j+1
        
        #sort to maximise '1' in the beginning
        return ''.join(sorted(res)[::-1])
        
