class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        cnt = 0
        
        for m in emails:
            local, domain = m.split("@")
            local = local.split("+")[0]
            local = local.split(".")
            local = "".join(local)
            
            mail = local+"@"+domain
            
            if mail not in seen:
                cnt+=1
            seen.add(mail)

        return cnt