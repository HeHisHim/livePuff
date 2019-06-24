# livePuff

## 查看文件夹下有几个文件
### ls | wc -w

## 删除后缀名为xxx的文件(可用正则筛选)
### find . -name "xxx" | xargs rm -rf
### 如 find . -name "*_aaa_*" , 筛选出文件名有aaa字段的文件, 再删除