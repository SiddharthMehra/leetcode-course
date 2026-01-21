class Solution:
    def numOfUnplacedFruits(self, fruits, baskets):
        n = len(baskets)
        N = 1
        while N<=n:
            N<<=1
        
        segmentTree = [0] * (2*N)

        for i in range(n):
            segmentTree[N+i] = baskets[i]
        
        #build segment tree bottom up
        for i in range(N-1, 0, -1):
            segmentTree[i] = max(segmentTree[2*i], segmentTree[2*i+1])
        
        count = 0
        for fruit in fruits:
            index = 1
            #if top index does not have enough fruit, no basket can have
            if segmentTree[index]<fruit:
                count+=1
                continue
            
            #2* index is left child, 2*index+1 is right child, binary search
            while index<N:
                if segmentTree[2*index]>=fruit:
                    index = 2* index
                else:
                    index = 2*index+1

            #mark used
            segmentTree[index]=-1

            #update segment tree bottom up
            while index>1:
                index//=2
                segmentTree[index] = max(segmentTree[2*index], segmentTree[2*index+1])
        
        return count
        
