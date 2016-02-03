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

================ mysql utf8: db connect tables ========================

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

====================== angular ajax data binding ======================

http://www.ng-newsletter.com/posts/beginner2expert-data-binding.html

$scope.$apply(updateClock); // what this means?

http://jimhoskins.com/2012/12/17/angularjs-and-apply.html

That step that checks to see if any binding values have changed actually has a method, $scope.$digest(). That’s actually where the magic happens, but we almost never call it directly, instead we use $scope.$apply() which will call $scope.$digest() for you.

$scope.$apply() takes a function or an Angular expression string, and executes it, then calls $scope.$digest() to update any bindings or watchers.

So, when do you need to call $apply()? Very rarely, actually. AngularJS actually calls almost all of your code within an $apply call. Events like ng-click, controller initialization, $http callbacks are all wrapped in $scope.$apply(). So you don’t need to call it yourself, in fact you can’t. Calling $apply inside $apply will throw an error.

You do need to use it if you are going to run code in a new turn. And only if that turn isn’t being created from a method in the AngularJS library. Inside that new turn, you should wrap your code in $scope.$apply(). Here is an example. We are using setTimeout, which will execute a function in a new turn after a delay. Since Angular doesn’t know about that new turn, the update will not be reflected.

==================== markdown editor ? =======================
https://github.com/zacharyvoase/markdoc/tree/master/src/markdoc


====================== bootstrap ======================
bootstrap is powerful, we should use it sometime, but not now.

================== UTC ==================
CREATE TABLE items (
    id serial primary key,
    author_id int references users,
    body text,
    created timestamp default (current_timestamp at time zone 'utc')
);

http://stackoverflow.com/questions/455580/json-datetime-between-python-and-javascript 

You can add the 'default' parameter to json.dumps to handle this:

date_handler = lambda obj: (
    obj.isoformat()
    if isinstance(obj, datetime.datetime)
    or isinstance(obj, datetime.date)
    else None
)
json.dumps(datetime.datetime.now(), default=date_handler)
'"2010-04-20T20:08:21.634121"'
Which is ISO 8601 format.

default(obj) is a function that should return a serializable version of obj or raise TypeError. The default simply raises TypeError.

======================== Markdown textarea ===========================
Copy from this example
http://wasilak.github.io/GitHub-flavored-markdown-with-angularjs-and-marked/

========================= sce.trustAsHtml ==========================
http://stackoverflow.com/questions/9381926/angularjs-insert-html-into-view
Insert HTML into view
For Angular 1.3, use ng-bind-html in the HTML:
<div ng-bind-html="thisCanBeusedInsideNgBindHtml"></div>
and use $sce.trustAsHtml() in the controller to convert the html string.
$scope.thisCanBeusedInsideNgBindHtml = $sce.trustAsHtml(someHtmlVar);

$sce is a service that provides Strict Contextual Escaping services to AngularJS.

===================== design =========================
1. index.html get 10 or 20 lastest articles; next page get older
2. click article to ajax show article and comments; if this article is comment of something , show that in some way
3. how to make a ajax url?
4. how to get latest 10 , and how next/
5. 


Rather than using your JavaScript to drive your URLs, let your URLs drive your JavaScript. Let the window.onhashchange event handler do all the work. Everything else should just change the hash.

You don't even need click handlers for links, just set the url to the right hash:

<a href="#red">Red</a>
Then, your hashchange handler takes care of the rest:

function hashChange() {
    var page = location.hash.slice(1);
    if (page) {
        $('#content').load(page+".html #sub-content");
        document.title = originalTitle + ' – ' + page;
        switch (page) {
            // page specific functionality goes here
            case "red":
            case "yellow":
                $("body").removeClass("red yellow").addClass(page);
                break;
        }
    }
}
The only reason to change the hash at all is if you want to be able to come back to the page and have it load the same state based on the URL. So, you already have the requirement to let the URL drive the JavaScript, right? Else why are you changing the hash? Moving functionality out of click handlers, and into the hashchange event only simplifies things.


# Building Nested Recursive Directives in Angular
http://sporto.github.io/blog/2013/06/24/nested-recursive-directives-in-angular/

# recursive template 
http://benfoster.io/blog/angularjs-recursive-templates
A much better solution is to use a template and render it recursively for each level in the tree. First we'll define an inline template:

<script type="text/ng-template" id="categoryTree">
    {{ category.title }}
    <ul ng-if="category.categories">
        <li ng-repeat="category in category.categories" ng-include="'categoryTree'">           
        </li>
    </ul>
</script>
For each category we display the title and then a nested list of its sub-categories by rendering the same template using ng-include.

The final task is to kick of the recursive template with our root categories:

<ul>
    <li ng-repeat="category in categories" ng-include="'categoryTree'"></li>
</ul>  


======================= web.py port ===================
python todo.py 1234 // listen on port 1234


====================== 解决web.py在SAE云中的Session使用问题 =========
http://www.cnblogs.com/chu888chu888/archive/2013/03/20/2971389.html

#是否具有调试功能
web.config.debug = False #一定要是False 不是的，如下
Sessions and Reloading/Debug Mode
Is your session data disappearing for seemingly no reason? This can happen when using the web.py app reloader (local debug mode), which will not persist the session object between reloads. Here's a nifty hack to get around this.

# Hack to make session play nice with the reloader (in debug mode)
if web.config.get('_session') is None:
    session = web.session.Session(app, db.SessionDBStore())
    web.config._session = session
else:
    session = web.config._session

DBStore. Session data is pickled and stored in a database. This can be useful if you want to store session data on a separate system. When creating, the DBStore takes 2 arguments: a web.py database instance, and the table name (string). The table which stores the session must have the following schema:

CREATE TABLE sessions(
    session_id CHAR(128) UNIQUE NOT NULL,
    atime timestamp NOT NULL default current_timestamp,
    data TEXT
);




# 【AngularJS系列7】路由概览
http://www.cnblogs.com/reeoo/p/3605045.html

ng的路由机制是靠ngRoute提供的，通过hash和history两种方式实现了路由，可以检测浏览器是否支持history来灵活调用相应的方式。ng的路由(ngRoute)是一个单独的模块，包含以下内容：

服务$routeProvider用来定义一个路由表，即地址栏与视图模板的映射
服务$routeParams保存了地址栏中的参数，例如{id : 1, name : 'tom'}
服务$route完成路由匹配，并且提供路由相关的属性访问及事件，如访问当前路由对应的controller
指令ngView用来在主视图中指定加载子视图的区域
以上内容再加上$location服务，我们就可以实现一个单页面应用了。

# AngularJS路由和模板
http://blog.fens.me/angularjs-route-template/
