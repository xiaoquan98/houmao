# Log

angular form is next step.   http://tutsnare.com/post-form-data-using-angularjs/

https://scotch.io/tutorials/submitting-ajax-forms-the-angularjs-way  how to submit form in Angular way, and json return format.
https://docs.angularjs.org/api/ng/service/$http   this example show how to use $http .

===================== utf8 ==========================
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

===================== mysql utf8: db connect tables ========================

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


======================== json format =============================

json return format : https://scotch.io/tutorials/submitting-ajax-forms-the-angularjs-way
data.errors
data.success 
data.message

The json library can parse JSON from strings or files. The library parses JSON into a Python dictionary or list. It can also convert Python dictionaries or lists into JSON strings.

So we can use a dict with errors success and message.


========================= finally statement =========================
why we need finally statement:

It makes a difference if you return early:

try:
    run_code1()
except TypeError:
    run_code2()
    return None   # The finally block is run before the method returns
finally:
    other_code()
Compare to this:

try:
    run_code1()
except TypeError:
    run_code2()
    return None   

other_code()  # This doesn't get run if there's an exception.
Other situations that can cause differences:

If an exception is thrown inside the except block.
If an exception is thrown in run_code1() but it's not a TypeError.
Other control flow statements such as continue and break statements.

======================== design restful api ============================
https://scotch.io/bar-talk/designing-a-restful-web-api

REST is basically a list of design rules that makes sure that an API is predictable and easy to understand and use.
Output format:json or xml? json.
Versioning: vX url prefix.

Let’s take a store locator API as an example. Here are some possible endpoints:

/v1/stores/1234 – Return the store that has id 1234
/v1/stores/1234/report – Report an error for the store with id 1234
/v1/stores – Return all stores
/v1/stores/near?lat=12.34&lon=-12.34 – Find stores near a given location
/v1/categories – Return a list of store categories

HTTP Verb    Description
GET    This is the most common verb, and is used to retrieve data
PUT    PUT requests are commonly used to update/replace or create an object
POST    This is used to create a new instance of an object, or update
DELETE    As the name suggests, this will delete the object

Timestamps
A widely-accepted standard for timestamps is ISO-8601. It is easy to read, easy to parse and it has great timezone support.

Error handling

Authentication
OAuth
HTTP Basic Authentication 
simply appending the API key to the query string

===================================================