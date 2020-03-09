'''
---创建名为address的数据库
create database address default charset utf8;

-- 切换到address数据库
use address;

--创建联系人表tb_contacter
create table tb_contacter
(
conid int auto_increment comment '编号',
conname varchar(31) not null comment '姓名',
contel varchar(15) default'' comment '邮箱',
primary key(conid)
);
'''

import pymysql

INSERT_CONTACTER = """
insert into tb_contacter (comname,contel,conemail)
values (%s,%s,%s)
"""

DELETE_CONTACTER = """
delete from tb_contacter where conid=%s
"""

UPDATE_CONTACTER = """
update tb_contacter set conname=%s, contel=%s, conemail=%s 
where conid=%s
"""

SELECT_CONTACTERS = """
select conid as id, conname as name, contel as tel, conemail as email 
from tb_contacter limit %s offset %s
"""
SELECT_CONTACTERS_BY_NAME = """
select conid as id, conname as name, contel as tel, conemail as email 
from tb_contacter where conname like %s
"""
COUNT_CONTACTERS = """
select count(conid) as total from tb_contacter
"""