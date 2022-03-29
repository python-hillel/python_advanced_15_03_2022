-- Comment
/*
Multi line 
comment
*/

/*
DDL - Data Definition Lang		CREATE, ALTER, DROP
DCL - Data Control Lang			GRANT, REVOKE
DML - Data Manipulation Lang	SELECT, INSERT, UPDATE, DELETE
*/


SELECT *
FROM customers
order by SupportRepId, FirstName;

select count(*)
from customers;


select count(*)
from tracks;

select *
from tracks;

create table TotalSizeByTrack as
select AlbumId, sum(Bytes) as TotalSize
from tracks
group by AlbumId
ORDER by 2 desc;


select AlbumId, Name, Bytes 
from tracks
where AlbumId in (1, 2, 3, 4)		-- > < = != <> >= <=   or anr not
-- order by AlbumId, Bytes
HAVING Bytes > 6000000;



select sum(TotalSize) as SuperTotalSize 
from (
select AlbumId, sum(Bytes) as TotalSize
from tracks
group by AlbumId
ORDER by 2 desc);


select AlbumId, sum(Bytes) as TotalSize
from tracks
where AlbumId in (1, 2, 3, 4)
group by AlbumId
having TotalSize > 8000000
order by TotalSize;


select *
from (
	select AlbumId, sum(Bytes) as TotalSize
	from tracks
	where AlbumId in (1, 2, 3, 4)
	group by AlbumId
) as res
where res.TotalSize > 8000000
order by res.TotalSize;




