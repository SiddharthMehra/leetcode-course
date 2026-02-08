class Solution:
    def findOrder(self, num_courses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        indegree = [0] * num_courses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course]+=1
        
        q = deque([i for i in range(num_courses) if indegree[i] == 0])
        result = []

        while q:
            course = q.popleft()
            result.append(course)
            
            for nei in graph[course]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    q.append(nei)

        if len(result) == num_courses:
            return result
        else:
            return []
