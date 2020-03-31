create database school;

-- \l
-- \c school

create table students (id Serial, name text, address text, age int);

-- \d
-- \d students

insert into students (name, address, age) values
  ('ryan', 'san francisco', 24);
insert into students (name, address, age) values
  ('joe', 'la', 30);

select * from students;
