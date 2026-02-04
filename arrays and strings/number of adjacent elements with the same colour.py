class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        colors = [0] * n
        count = 0
        answer = []

        for index, color in queries:

            if index>0 and colors[index]!=0 and colors[index] == colors[index-1]:
                count-=1
            
            if index<n-1 and colors[index]!=0 and colors[index] == colors[index+1]:
                count-=1
            
            colors[index] = color

            #add new pairs
            if index>0 and colors[index] == colors[index-1]:
                count+=1
            
            if index<n-1 and colors[index] == colors[index+1]:
                count+=1
            
            answer.append(count)
        
        return answer
        
