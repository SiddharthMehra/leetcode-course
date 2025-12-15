class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        q = deque([(startGene, 0)])
        seen = {startGene}
        
        while q:
            current, steps = q.popleft()
            if current == endGene:
                return steps
            
            for c in "AGCT":
                for i in range(len(current)):
                    neighbor = current[:i] + c + current[i+1:]
                    if neighbor not in seen and neighbor in bank:
                        seen.add(neighbor)
                        q.append((neighbor, steps+1))
        
        return -1
                        
        
