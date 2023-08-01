# Write your MySQL query statement below
select s.id
from  Weather s join Weather w
on datediff(s.recordDate, w.recordDate) = 1 and s.temperature-w.temperature > 0;