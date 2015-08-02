# mysql basic

MySQL is an open-source relational database. In a nutshell, for those unfamiliar with it: A database is where an application keeps its stuff.

# install

> sudo aptitude update
> sudo aptitude install mysql-server

> sudo service mysql start   // launch 
> sudo /usr/sbin/update-rc.d mysql defaults  // launching at boot 

> /usr/bin/mysql -u root -p  // open mysql shell

# mysql shell 

> UPDATE mysql.user SET Password = PASSWORD('password') WHERE User = 'root'; // set password 
> FLUSH PRIVILEGES; // make change go into effect

> SELECT User, Host, Password FROM mysql.user;  // looking at users

> CREATE DATABASE demodb;
> INSERT INTO mysql.user (User,Host,Password) VALUES('demouser','localhost',PASSWORD('demopassword'));
> FLUSH PRIVILEGES;
> GRANT ALL PRIVILEGES ON demodb.* to demouser@localhost;
> FLUSH PRIVILEGES;

# python & mysql

install mysql  client
install  python interface