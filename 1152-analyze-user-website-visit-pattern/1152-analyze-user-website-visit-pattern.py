class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        mapping = defaultdict(list)
        
        lst = []
        
        for name,t,site in zip(username,timestamp,website):
            lst.append((name,t,site))
        
        lst.sort(key=lambda x:(x[0],x[1]))
        
        for name,t,site in lst:
            mapping[name].append(site)
                
        result = defaultdict()
        
        for k,v in mapping.items():
            pairs = Counter(set(combinations(v,3)))
            print(k,pairs)
            for p in pairs:
                result[tuple(p)]=1+result.get(tuple(p),0)
            
        mx = 0
        res = None
        print(result)
        for k,v in result.items():
            if v >= mx:
                if v > mx:
                    mx = v
                    res = k
                elif v == mx:
                    res = min(res, k)

        return res
#         users = defaultdict(list)
# 	    # It is not necessary to use defaultdict here, we can manually create dictionaries too
		
#         for user, time, site in sorted(zip(username, timestamp, website), key = lambda x: (x[0],x[1])):    
#             users[user].append(site)     # defaultdicts simplify and optimize code

#         patterns = Counter()   # this can also be replaced with a manually created dictionary of counts
		
# 		# Get unique 3-sequence (note that website order will automatically be maintained)
# 		# Note that we take the set of each 3-sequence for each user as they may have repeats
# 		# For each 3-sequence, count number of users
		
#         for user, sites in users.items():
#             print(sites,  Counter(set(combinations(sites, 3))))
#             patterns.update(Counter(set(combinations(sites, 3))))     
		
# 		# Re-iterating above step for clarity
# 		# 1. first get all possible 3-sequences combinations(sites, 3)
# 		# 2. then, count each one once (set)
# 		# 3. finally, count the number of times we've seen the 3-sequence for every user (patterns.update(Counter)) 
# 		# - updating a dictionary will update the value for existing keys accordingly (int in this case)
		
# 		# An expanded version of the above step is given below.
			
#         print("final" , patterns)  # sanity check
	
# 		# get most frequent 3-sequence sorted lexicographically
#         return max(sorted(patterns), key=patterns.get)