create database myissuedb default character set utf8 collate utf8_general_ci;

CREATE TABLE issue(
	id INT AUTO_INCREMENT,
	title TEXT,
	detail TEXT,
	parent INT ,
	user INT,
	isArticle BOOLEAN,
	primary key(id)
)DEFAULT CHARSET=utf8;

CREATE TABLE user(
	id INT AUTO_INCREMENT,
	name TEXT,
	primary key(id)
)DEFAULT CHARSET=utf8;