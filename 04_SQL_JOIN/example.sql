-- SELECT

-- UPDATE, INSERT, DELETE

INSERT INTO customers (FirstName, LastName)
VALUES
	('Mike1', 'Twen1'),
	('Mike2', 'Twen2'),
	('Mike3', 'Twen3'),
	('Mike4', 'Twen4'),
	('Mike5', 'Twen5');


INSERT INTO customers (FirstName, LastName, City, Country)
SELECT FirstName, LastName, City, Country
FROM employees;


-- UPDATE customers SET Country = 'USA';
UPDATE customers SET Country = 'USA' WHERE CustomerId in (53, 57, 60);

DELETE FROM customers WHERE CustomerId >= 60 and CustomerId <= 72;
DELETE FROM customers WHERE CustomerId BETWEEN 60 AND  72;

DELETE FROM customers WHERE CustomerId IN (SELECT CustomerId FROM customers WHERE SupportRepId IS NULL);

-- DROP TABLE customers;


select CustomerId
from customers
where FirstName = 'Lucas' and LastName = 'Mancini';


select *
from invoices
where CustomerId = 47;


select c.FirstName, c.LastName, i.InvoiceDate, i.BillingAddress, i.Total
from customers as c
	join invoices as i on c.CustomerId = i.CustomerId
where c.FirstName = 'Lucas' and c.LastName = 'Mancini'


select count(*)		-- 412
from customers as c
	join invoices as i on c.CustomerId = i.CustomerId;

select *		-- 420
from customers as c
	left join invoices as i on c.CustomerId = i.CustomerId
where i.InvoiceId is null
;


select *		-- 420
from invoices as c
	left join customers as i on c.CustomerId = i.CustomerId
where i.CustomerId is null
;


select count(*) from invoices;
select count(*) from customers;


insert into albums (Title, ArtistId) values ('Album 1', 300);

PRAGMA foreign_keys = On;

select *
from artists as art
	join albums as al on art.ArtistId = al.ArtistId
where art.Name = 'Alice In Chains';

delete from artists where ArtistId = 5;

delete from albums where AlbumId = 7;

delete from tracks where AlbumId = 7;




/*
 * 		One - 2 - One
 *
 * 		One - 2 - Many
 *
 * 		Many - 2 - Many
 *
 */
