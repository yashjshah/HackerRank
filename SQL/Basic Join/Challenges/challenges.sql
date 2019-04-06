select c.hacker_id, h.name ,count(c.hacker_id) as c_count
from Hackers as h
    inner join Challenges as c on c.hacker_id = h.hacker_id
group by c.hacker_id
having 
    c_count = 
        (SELECT MAX(temp1.cnt)
        from (SELECT COUNT(hacker_id) as cnt
             from Challenges
             group by hacker_id
             order by hacker_id) temp1)
    or c_count in 
        (select t.cnt
         from (select count(*) as cnt 
               from challenges
               group by hacker_id) t
         group by t.cnt
         having count(t.cnt) = 1)
order by c_count DESC, c.hacker_id
;