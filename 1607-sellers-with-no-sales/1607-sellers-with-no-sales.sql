# Write your MySQL query statement below

select seller_name from Seller
where seller_id not in (
    select seller_id from Orders o
    where year(o.sale_date) = 2020)
order by seller_name;