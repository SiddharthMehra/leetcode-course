class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:

        def parse(s):
            res = []
            i = 0

            while i<len(s):
                #if not part of key, just append it
                if s[i]!='%':
                    res.append(s[i])
                    i+=1
                
                else:
                    #recursive inside keys value
                    if '%' in keys[s[i+1]]:
                        keys[s[i+1]] = parse(keys[s[i+1]])
                    res.append(keys[s[i+1]])
                    i+=3
            
            return ''.join(res)
        
        keys = defaultdict(str)
        for k,v in replacements:
            keys[k] = v
        
        return parse(text)
                    
                
        
