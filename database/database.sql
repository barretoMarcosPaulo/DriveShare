use drive;
create table users(
	id int primary key auto_increment,
    primaryName varchar(100) not null,
    lastName varchar(100) not null,
    email varchar(100) not null,
    passwd varchar(100) not null
);
select*from users;
drop table users;
