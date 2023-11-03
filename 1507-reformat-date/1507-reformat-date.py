class Solution:
    def reformatDate(self, date: str) -> str:
        month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        
        dd,mm,yy = date.split(" ")
        dd = dd[:-2]
        
        return yy + "-" + ("0"+str(month.index(mm)+1))[-2:] + "-" + ("0"+dd)[-2:]
    
        """
        mapping
        
        20th to 20
        oct to month date
        year direct no ds
        
        """ 