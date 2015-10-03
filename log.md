# Log

angular form is next step.   http://tutsnare.com/post-form-data-using-angularjs/

https://scotch.io/tutorials/submitting-ajax-forms-the-angularjs-way  how to submit form in Angular way, and json return format.
https://docs.angularjs.org/api/ng/service/$http   this example show how to use $http .

===============================================
最开始没注意数据库的编码，使用默认的方式去连接：
db = web.database(dbn='mysql', user='root', pw='lihuipeng007', host='localhost', db='test')  
  
sql = '''''''select * from tb_admin_user where login='%s' and password='%s' ''' % (username, password)  
result = db.query(sql)  
print result[0]['name']  
这样打印出来就会乱码
后来在数据库连接及打印的时候加上编码转换后就正常：
db = web.database(dbn='mysql', user='root', pw='lihuipeng007', host='localhost', db='test', charset='latin1')  
  
sql = '''''select * from tb_admin_user where login='%s' and password='%s' ''' % (username, password)  
result = db.query(sql)  
print result[0]['name'].encode('latin1','ignore') 
最后放上服务器测试的时候发现还是会乱码，报的是这个错误：
UnicodeDecodeError: 'ascii' codec can't decode byte 0xe9 in position 0: ordinal not in range(128)
然后在文件前面加入：
import sys 
default_encoding = 'utf-8' 
if sys.getdefaultencoding() != default_encoding: 
    reload(sys) 
    sys.setdefaultencoding(default_encoding) 
中文显示终于正常了~~~不容易啊。。

=============================================

1、检查并修改mysql的my.ini的配置文件

复制代码 代码如下:

default-character-set=utf8
2、建立数据库是要指定字符集

复制代码 代码如下:

create database mydb default character set utf8 collate utf8_general_ci;
3、建立数据表示也要指定字符集：
出问题的命令： 

复制代码 代码如下:

CREATE TABLE IF NOT EXISTS `mydb` ( 
  `username` varchar(64) NOT NULL, 
  `userid` int(11) NOT NULL, 
 ) ENGINE=InnoDB DEFAULT CHARSET=latin1; 
  
正确的命令： 
复制代码 代码如下:

CREATE TABLE IF NOT EXISTS `mydb` ( 
  `username` varchar(64) NOT NULL, 
  `userid` int(11) NOT NULL, 
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
说明：mysql版本：5.5.24

=====================================================

json return format : https://scotch.io/tutorials/submitting-ajax-forms-the-angularjs-way
data.errors
data.success 
data.message
