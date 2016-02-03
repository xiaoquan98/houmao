create database myissuedb default character set utf8 collate utf8_general_ci;

CREATE TABLE issue(
    id INT AUTO_INCREMENT,
    title TEXT,
    detail TEXT,
    parent INT ,
    user INT,
    isArticle BOOLEAN,
    created timestamp default current_timestamp,
    modified timestamp default current_timestamp on update current_timestamp,
    primary key(id)
)DEFAULT CHARSET=utf8;

CREATE TABLE user(
    id INT AUTO_INCREMENT,
    name TEXT,
    password TEXT,
    primary key(id)
)DEFAULT CHARSET=utf8;

drop table issue;// to remove table

CREATE TABLE sessions(
    session_id CHAR(128) UNIQUE NOT NULL,
    atime timestamp NOT NULL default current_timestamp,
    data TEXT
);