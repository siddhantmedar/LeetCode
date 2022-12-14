class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        mp = dict()
        
        for i in range(len(messages)):
            mp[senders[i]] = len(messages[i].split())+mp.get(senders[i],0)

        mx = float("-inf")
        result = None
        
        for k,v in mp.items():
            if v >= mx:
                if v > mx or (v == mx and k > result):
                    result = k
                    mx = v
        
        return result