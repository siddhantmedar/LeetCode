class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        curr = 0
        
        idle = [(ele,i) for i,ele in enumerate(servers)]
        busy = []
        
        heapq.heapify(idle)
        
        res = []
        
        for curr,task in enumerate(tasks):
            while busy and busy[0][0] <= curr:
                _,e,i = heapq.heappop(busy)
                heapq.heappush(idle,(e,i))
            
            if idle: 
                e,i = heapq.heappop(idle)
                res.append(i)
                heapq.heappush(busy,(curr+task,e,i))

            else:
                t,e,i = heapq.heappop(busy)
                res.append(i)
                heapq.heappush(busy,(t+task,e,i))

        
        return res