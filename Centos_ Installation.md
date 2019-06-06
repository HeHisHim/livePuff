## **`Centos7 装机必备`**

### The script virtualenv is installed in which is not on PATH
    vim ~/.bashrc
    在最后一行加上  export PATH="/usr/lib64/python3/bin:$PATH"
    source ~/.bashrc

## shadowsocks - (https://www.freeluffy.com/ss-server-on-vultr/)
1. wget –no-check-certificate -O shadowsocks.sh https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowsocks.sh
2. chmod +x shadowsocks.sh
3. ./shadowsocks.sh 2>&1 | tee shadowsocks.log

## nginx
1. yum install -y pcre pcre-devel
2. yum install -y zlib zlib-devel
3. yum install -y openssl openssl-devel
4. wget https://nginx.org/download/nginx-1.16.0.tar.gz
5. tar -zxvf nginx-1.16.0.tar.gz / cd nginx-1.16.0
6. ./configure
7. make / make install
8. whereis nginx

## supervisor

## python3
1. yum -y groupinstall "Development tools"
2. yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
3. yum install libffi-devel -y
4. mkdir /usr/lib64/python3 -- 跟系统python目录一致
4. wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tar.xz -- 先放进临时文件里, 再编译放进/usr/lib64/python3
5. tar -xvJf Python-3.7.3.tar.xz
6. cd Python-3.7.3
7. ./configure --prefix=/usr/lib64/python3
8. make && make install
9. ln -s /usr/lib64/python3/bin/python3.7 /usr/bin/python3

* ModuleNotFoundError: No module named '_ctypes'
1. yum install libffi-devel -y

## mongodb [https://www.mongodb.com/download-center/community] RHEL 7.0 Linux 64-bit x64
1. wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-4.0.10.tgz
2. tar zxf mongodb-linux-x86_64-4.0.10.tgz
3. mkdir /usr/local/mongodb
4. mv mongodb-linux-x86_64-4.0.10/* /usr/local/mongodb
5. mkdir data / mkdir db
6. mkdir logs / touch mongo.log
7. vim mongodb.conf
    * dbpath=/usr/local/mongodb/data/db/
    * logpath=/usr/local/mongodb/logs/mongo.log
    * logappend=true
    * port=27017
    * fork=true
8. ./bin/mongod -f mongodb.conf

## redis
1. wget http://download.redis.io/redis-stable.tar.gz
2. tar zxf redis-stable.tar.gz
3. cd redis-stable
4. make && make PREFIX=/usr/local/redis install
5. cp redis.conf /usr/local/redis/bin

* 设置后台启动: daemonize yes
* 设置密码: requirepass ***
* 设置远程连接: 注释 bind

## mariadb
### 改源
1. cd /etc/yum.repos.d
2. vi MariaDB.repo
    * [mariadb]
    * name = MariaDB
    * baseurl = http://yum.mariadb.org/10.2/centos7-amd64
    * gpgkey = https://yum.mariadb.org/RPM-GPG-KEY-MariaDB
    * gpgcheck = 1

3. yum install MariaDB-server MariaDB-client
4. systemctl start mysqld
5. mysql_secure_installation -- 配置
6. 其他配置
    * Remove anonymous users? [Y/n] <– 是否删除匿名用户, 回车

    * Disallow root login remotely? [Y/n] <–是否禁止root远程登录, 回车,

    * Remove test database and access to it? [Y/n] <– 是否删除test数据库, 回车

    * Reload privilege tables now? [Y/n] <– 是否重新加载权限表, 回车