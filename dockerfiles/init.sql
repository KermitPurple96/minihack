

CREATE USER 'mini3'@'%' IDENTIFIED BY 'tjnKy82fHxO4TUJFcPLo6wmvd';
GRANT SELECT ON minihack.* TO 'mini3'@'%';

create database if not exists minihack;
use minihack;
create table secrets (
	flag varchar(50)
);

insert into secrets (flag) values ('T0ipt5K8k31dmNMDOH4WsxeV9');
