# livePuff

# Linux command

### 查看文件夹下有几个文件
```linux
ls | wc -w
```

### 删除后缀名为xxx的文件(可用正则筛选)
```linux
find . -name "xxx" | xargs rm -rf
```
#### 如 find . -name "\*\_aaa\_\*" , 筛选出文件名有aaa字段的文件, 再删除

### 查找目录下按具体时间过滤的文件
```linux
ls --full-time *_jpg_* | sed -n '/2019-07-02/p'
```
#### 查询在2019年7月2号被改动的jpg文件

### 查找目录下某文件的修改时间
```linux
ll | grep xxx
```

# git

### 使用git merge --squash合并代码(假设是将feature合并到master)
#### 切换到想要合并的分支(切换前确保开发分支已提交), 并拉取最新的代码
```git
git checkout master
git pull origin master:master
```
#### git合并
```
git merge --squash feature
```
#### 此时有冲突需手动解决冲突
```git
git status 查看有冲突的文件并解决冲突
git add ConflictFile 添加已解决冲突的文件
```
#### git提交, 推送
```git
git commit -m "merge feature branch into master"
git push origin master:master
```

# MySQL

### 解决A LEFT JOIN B 连接得到的新表C, 查询出来的记录总条数多于A表的记录总条数
#### 原因是A与B的关系不是1:1或1:0, 而是1:n(n > 1)导致A对应到B产生了多条数据. 此时要先处理B中重复的数据再与A做连接
```Mysql
SELECT A.xid, C.yid FROM xtable AS A LEFT JOIN (SELECT B.yid FROM ytable AS B GROUP BY B.yid) AS C ON A.xid = C.yid
```

