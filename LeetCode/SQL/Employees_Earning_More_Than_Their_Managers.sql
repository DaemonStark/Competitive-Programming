-- LeetCode - Employees Earning More Than Their Managers Solution
-- MySQL
select a.name as Employee from Employee a LEFT JOIN Employee b on a.managerId = b.id where a.salary > b.salary;
