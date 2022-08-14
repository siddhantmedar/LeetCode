class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        num = []
        
        for i in range(len(logs)):
            tmp = logs[i].split()
            if tmp[1].isalpha():
                letters.append((" ".join(tmp[1:]), tmp[0]))
            else:
                num.append(logs[i])
                
        letters.sort()
        
        return [letter[1] + " " + letter[0] for letter in letters] + num