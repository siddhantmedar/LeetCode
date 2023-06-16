class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        cnt = 0
        
        for m in emails:
            local, domain = m.split("@")
            local = "".join((local.split("+")[0]).split("."))
            mail = local+"@"+domain
            
            if mail not in seen:
                cnt+=1
            seen.add(mail)

        return cnt