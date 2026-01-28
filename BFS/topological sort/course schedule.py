class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        indegree = [0] * numCourses

        adj = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course]+=1
        
        #append courses with no dependence
        q = [i for i in range(numCourses) if indegree[i] == 0]

        courses_processed = 0

        while q:
            
            #no dependence course, so pop from the queue and add to processed
            curr = q.pop()
            courses_processed+=1

            #remove dependency from the popped course
            for neighbor in adj[curr]:
                indegree[neighbor]-=1

                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        return courses_processed == numCourses





