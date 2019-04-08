### [删除github不小心提交了敏感信息的文件和提交记录](https://www.jianshu.com/p/d8c6951c0aba)

### 1. cd 项目
### 2. 执行git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch 敏感文件名' --prune-empty --tag-name-filter cat -- --all
### 3. 可以将敏感文件名添加进.gitignore, 防止再次提交
### 4. 如果确保不会push不会发生冲突，可以使用 git push origin --force --all