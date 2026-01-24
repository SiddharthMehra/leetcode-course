class WordDistance:

    def __init__(self, wordsDict: List[str]):

        self.d = defaultdict(list)

        for i, word in enumerate(wordsDict):
            self.d[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:

        indices1 = self.d[word1]
        indices2 = self.d[word2]

        i, j, dist = 0, 0, float('inf')
        while i<len(indices1) and j<len(indices2):
            dist = min(dist, abs(indices1[i] - indices2[j]))

            if indices1[i] == indices2[j]:
                return 0
            elif indices1[i]<indices2[j]:
                i+=1
            else:
                j+=1
        
        return dist
        
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
