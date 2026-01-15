class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        k = len(words)
        word_length = len(words[0])
        substring_size = word_length * k
        word_count = Counter(words)

        def sliding_window(left):
            words_found = defaultdict(int)
            words_used = 0
            excess_word = False

            for right in range(left, n, word_length):
                if right + word_length>n:
                    break
                
                sub = s[right:right + word_length]
                #reset window
                if sub not in word_count:
                    words_found = defaultdict(int)
                    words_used = 0
                    excess_word = False
                    left = right + word_length
                
                else:
                    #if we reached max window size or have an excess word, remove the current word from the window
                    while right-left == substring_size or excess_word:
                        leftmost_word = s[left:left+word_length]
                        left+=word_length
                        words_found[leftmost_word]-=1
                    
                        if (words_found[leftmost_word] == word_count[leftmost_word]):       
                        #this was the excess word
                            excess_word = False
                    
                        else:
                        #otherwise we needed it
                            words_used-=1
                
                    words_found[sub]+=1
                    if words_found[sub]<=word_count[sub]:
                        words_used+=1
                
                    else:
                        excess_word = True
                
                    if words_used == k and not excess_word:
                        ans.append(left)
        
        ans = []
        for i in range(word_length):
            sliding_window(i)
        
        return ans
                    
                    


        
