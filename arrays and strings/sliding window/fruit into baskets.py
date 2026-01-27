class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        count = defaultdict(int)

        l, total, res = 0, 0, 0
        for r in range(len(fruits)):
            count[fruits[r]]+=1
            total+=1
            #shrink the window
            while len(count)>2:
                count[fruits[l]]-=1
                total-=1

                if not count[fruits[l]]:
                    del count[fruits[l]]
                
                l+=1


            res = max(res, total)
        
        return res
