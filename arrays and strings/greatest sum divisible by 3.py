class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:

        #track the minimum numbers where %2==1 and %2 ==2


        total = 0
        #for remainder 1
        min1_1 = min1_2 = float('inf')
        #for remainder 2
        min2_1 = min2_2 = float('inf')

        for x in nums:
            total+=x
            r = x%3

            if r==1:
                if x<min1_1:
                    min1_2 = min1_1
                    min1_1 = x
                elif x<min1_2:
                    min1_2 = x
                
            elif r == 2:
                if x<min2_1:
                    min2_2 = min2_1
                    min2_1 = x
                elif x<min2_2:
                    min2_2 = x
                
        r = total%3
        if r==0:
            return total
        
        if r == 1:
            remove_1 = min1_1
            remove_2 = min2_1 + min2_2
            remove = min(remove_1, remove_2)
            return total - remove if remove<float('inf') else 0
        
        if r==2:
            remove1 = min2_1
            remove2 = min1_1 + min1_2
            remove = min(remove1, remove2)
            return total - remove if remove<float('inf') else 0
