# Write your MySQL query statement below
select name
from Employee s
where s.id in 
(select e.managerId
from Employee e
group by e.managerId
having count(*) >= 5);