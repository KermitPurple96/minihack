

CREATE USER 'mini2'@'%' IDENTIFIED BY 'T0ipt5K8k31dmNMDOH4WsxeV9';
GRANT SELECT ON minihack.* TO 'mini2'@'%';

create database if not exists minihack;
use minihack;
create table secrets (
	flag varchar(50)
);

insert into secrets (flag) values ('rFHDxsMCwRES1i5I84JjdLO9b');
