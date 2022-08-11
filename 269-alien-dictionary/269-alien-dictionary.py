class Solution:
    def alienOrder(self, words: List[str]) -> str:
        def toposort():
            count = 0
            res = ""
            q = deque([k for k,v in indegree.items() if v == 0])
            
            while q:
                n = len(q)
                for k in range(n):
                    node = q.popleft()
                    res+=node
                    count+=1
                    
                    if node in graph:
                        for nei in graph[node]:
                            indegree[nei]-=1
                            if indegree[nei] == 0:
                                q.append(nei)
        
            return res if count == len(indegree) else ""
        
        graph = defaultdict(set)
        indegree = {c:0 for word in words for c in word}
        
        for i in range(len(words)-1):
            word1, word2 = words[i], words[i+1]
            mn = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:mn] == word2[:mn]:
                return ""
            
            for j in range(mn):
                if word1[j] != word2[j]:
                    if word2[j] not in graph[word1[j]]:
                        graph[word1[j]].add(word2[j])
                        indegree[word2[j]] = 1+indegree.get(word2[j],0)
                    break
        
        result = toposort()
        
        return result