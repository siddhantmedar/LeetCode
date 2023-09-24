class MagicDictionary:

    def __init__(self):
        self.mp = defaultdict(list)
        
    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.mp[len(word)].append(word)

    def search(self, searchWord: str) -> bool:
        nei = self.mp[len(searchWord)]
        
        answer = False
        
        for word in nei:
            if answer:
                break
            
            diff = 0
            
            for a,b in zip(searchWord,word):
                if a!=b:
                    diff+=1
            
            # print(sum(cont),"".join(word),"".join(searchWord),cont)
            if diff == 1:
                answer = True
            if answer:
                print("".join(word),"".join(searchWord))
        return answer

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)