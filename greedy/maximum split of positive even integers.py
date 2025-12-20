class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        ans, i = [], 2
        if finalSum%2==0:
            while i<=finalSum:
                ans.append(i)
                finalSum-=i
                i+=2
            #add the balance to the end since you cannot add any number
            ans[-1]+=finalSum
        
        return ans
