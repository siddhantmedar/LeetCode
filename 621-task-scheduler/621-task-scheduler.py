class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mp = {}
        
        for i,ele in enumerate(tasks):
            mp[ele] = 1+mp.get(ele, 0)
        
        heap = [-1*v for _, v in mp.items()]
        
        heapq.heapify(heap)
        
        q = deque()
        
        time = 0
        
        while heap or q:
            if heap:
                task = -1*heapq.heappop(heap)
                
                time+=1
                
                task-=1
                
                if task:
                    q.append((time+n, task))
                
            else:
                time+=1
                
            if q and q[0][0] == time:
                heapq.heappush(heap, -1*q[0][1])
                q.popleft()
                
        return time