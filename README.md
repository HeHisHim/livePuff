# livePuff

# Linux command

### 查看文件夹下有几个文件
```linux
ls | wc -w
```

### 删除后缀名为xxx的文件(可用正则筛选)
```
find . -name "xxx" | xargs rm -rf
```
#### 如 find . -name "\*\_aaa\_\*" , 筛选出文件名有aaa字段的文件, 再删除

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
```
git commit -m "merge feature branch into master"
git push origin master:master
```


