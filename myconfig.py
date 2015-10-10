# -*- coding: utf-8 -*-
NUMBER_IN_PAGE = 10
CREATEDB_QUERY ="create database myissuedb default character set utf8 collate utf8_general_ci;"

CREATETB_QUERY_ISSUE = """CREATE TABLE issue(
    id INT AUTO_INCREMENT primary key,
    title TEXT,
    detail TEXT,
    parent INT ,
    authorId INT,
    isArticle BOOLEAN,
    created timestamp default current_timestamp
)DEFAULT CHARSET=utf8;"""

CREATETB_QUERY_USER = """CREATE TABLE user(
    id INT AUTO_INCREMENT,
    name TEXT,
    password TEXT,
    primary key(id)
)DEFAULT CHARSET=utf8;"""

#drop table issue;// to remove table
