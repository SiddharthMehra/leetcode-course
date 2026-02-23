class Solution:
    def minMovesToMakePalindrome(self, s):

        s = list(s)
        n= len(s)
        left, right = 0, n-1
        moves = 0

        while left<right:
            if s[left] == s[right]:
                left+=1
                right-=1
            
            else:
                k = right
                while k>left and s[k]!=s[left]:
                    k-=1
                
                if k == left:
                    #this is the middle character
                    s[left], s[left+1] = s[left+1], s[left]
                    moves+=1
                
                #bubble towards right
                else:
                    while k<right:
                        s[k], s[k+1] = s[k+1], s[k]
                        moves+=1
                        k+=1
                    
                    left+=1
                    right-=1
            
        return moves

                
