drop database if exists groupon;
create database groupon charset utf8;
use groupon;

/* InnoDB engine is required if you want to use foreign key.  */
set storage_engine = InnoDB;

set names 'utf8';

create table sites (
    id int auto_increment not NULL,
    name varchar(20) not NULL,
    url varchar(255) not NULL,
    primary key(id)
) charset utf8;

create table cities (
    id int auto_increment not NULL,
    name char(20) unique not NULL,
    primary key(id)
) charset utf8;

create table deals (
    id int auto_increment not NULL,
    url varchar(255) not NULL,
    title varchar(500) not NULL,
    price float not NULL,
    original_price float not NULL,
    detail text not NULL,
    time timestamp,
    city_id int not NULL,
    site_id int not NULL,
    primary key(id),
    foreign key (city_id) references cities(id)
    on update cascade on delete cascade,
    foreign key (site_id) references sites(id)
    on update cascade on delete cascade
) charset utf8;

insert into cities(name) values ('安庆'),
	('北京'),
	('长春'), ('长沙'), 	('常州'), ('成都'),	('重庆'),
	('东莞'), ('大连'), ('东营'),
	('鄂州'),
	('福州'),
	('广州'), ('贵阳'),
	('哈尔滨'), 	('杭州'), ('合肥'), ('衡阳'), ('惠州'),
    ('济南'), ('济宁'), ('金华'),
    ('昆明'),
    ('兰州'), ('连云港'), ('临沂'),
    ('南昌'), ('南京'), ('南宁'), ('南通'), ('宁波'),
    ('青岛'),
    ('上海'), ('邵阳'), ('绍兴'), ('深圳'), ('沈阳'), ('石家庄'),
    ('苏州'),
    ('太原'), ('天津'),
    ('威海'), ('潍坊'), ('温州'), ('无锡'), ('武汉'), ('芜湖'),
    ('西安'), ('厦门'), ('湘潭'), ('襄樊'), ('徐州'),
    ('烟台'), ('盐城'), ('扬州'), ('宜昌'),
    ('镇江'), ('郑州'), ('中山'), ('珠海'), ('淄博'),
    ('其它');
           
insert into sites(name, url) values('美团网', 'http://www.meituan.com'),
       ('爱帮网', 'http://tuan.aibang.com'),
       ('爱赴团', 'http://www.ftuan.com'),
       ('满座网', 'http://www.manzuo.com'),
       ('团宝网', 'http://www.groupon.cn'),
       ('窝窝团', 'http://www.55tuan.com');
