-- Questão interessante
create table teste1(a int not null primary key, b char(1));
create table teste2(a int not null primary key, c int);
insert into teste1(a,b) values(10, 'A');
insert into teste1(a,b) values(11, 'B');
insert into teste1(a,b) values(12, 'C');
insert into teste1(a,b) values(14, 'D');
insert into teste2(a,c) values(10, 7);
insert into teste2(a,c) values(11, 9);
insert into teste2(a) values(15);

select * from teste1;
select * from teste2;

select t2.a, t2.c
from teste1 as t1 
left join teste2 as t2
on t1.a = t2.a