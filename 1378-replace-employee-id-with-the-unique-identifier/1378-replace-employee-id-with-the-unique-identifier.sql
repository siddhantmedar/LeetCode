# Write your MySQL query statement below
select r.unique_id, l.name from Employees l left join EmployeeUNI r on l.id = r.id;