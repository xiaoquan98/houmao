CREATE TABLE todo (    id INT AUTO_INCREMENT,    title TEXT,    primary key (id));

CREATE TABLE todo(
	id INT AUTO_INCREMENT,
	title TEXT,
	detail TEXT,
	parent INT ,
	user INT,
	isArticle BOOLEAN,
	primary key(id)
);

CREATE TABLE user(
	id INT AUTO_INCREMENT,
	name TEXT,
	primary key(id)
);