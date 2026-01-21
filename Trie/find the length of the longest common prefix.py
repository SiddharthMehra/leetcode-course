class TrieNode():
    def __init__(self):
        self.children = {}
    

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, num):

        #insert number digit by digit
        node = self.root
        for ch in str(num):
            if ch not in node.children:
                node.children[ch] = TrieNode()
            
            node = node.children[ch]
    
    def longest_prefix_length(self, num):
        #longest prefix of num which exists in the tree
        node = self.root
        length = 0

        for ch in str(num):
            if ch not in node.children:
                break
            
            node = node.children[ch]
            length+=1
        
        return length
    

class Solution:
    def longestCommonPrefix(self, arr1, arr2):
        trie = Trie()

        for num in arr1:
            trie.insert(num)
        
        ans = 0
        for num in arr2:
            ans = max(ans, trie.longest_prefix_length(num))
        
        return ans
