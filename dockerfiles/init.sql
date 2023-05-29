

CREATE USER 'mini2'@'%' IDENTIFIED BY 'tjnKy82fHxO4TUJFcPLo6wmvd';
GRANT SELECT ON minihack.* TO 'mini2'@'%';

create database if not exists minihack;
use minihack;
create table secrets (
	flag varchar(50)
);

insert into secrets (flag) values ('rFHDxsMCwRES1i5I84JjdLO9b');
