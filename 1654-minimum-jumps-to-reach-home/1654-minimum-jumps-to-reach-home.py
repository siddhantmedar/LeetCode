class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)
        
        level = 0
        
        visited = set()
        q = deque([(0,False)])
        
        visited.add((0,False))
        
        while q:
            n = len(q)
            
            for _ in range(n):
                idx,last_backward = q.popleft()
                
                if idx == x:
                    return level
                
                next_pos = idx+a
                if next_pos not in forbidden and next_pos < 6000 and (next_pos,False) not in visited:
                    visited.add((next_pos,False))
                    q.append((next_pos,False))
                
                if not last_backward:
                    next_pos = idx-b
                    if next_pos not in forbidden and next_pos >= 0 and (next_pos,True) not in visited:
                        visited.add((next_pos,True))
                        q.append((next_pos,True))
            
            level+=1
    
        print(level)
        
        return -1