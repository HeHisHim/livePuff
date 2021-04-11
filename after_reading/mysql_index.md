### [MySQL索引创建及使用](https://blog.csdn.net/dengchenrong/article/details/88425762)

## **`MySQL索引概念`**
* 索引是一种特殊的文件(InnoDB数据表上的索引是表空间的一个组成部分), 它们包含着对数据表里所有记录的引用指针. 更通俗的说, 数据库索引好比是一本书前面的目录, 能加快数据库的查询速度. 有了相应的索引之后, 数据库会直接在索引中查找符合条件的选项

## **`索引类型`**
## **`普通索引`**
* 普通索引是最基本的索引, 它没有任何限制, 是大多数时候用到的索引
    ## **`创建方式`**
    1. 直接创建: CREATE INDEX indexName ON table_name (column_name)
    2. 修改表结构的方式添加索引: ALTER table tableName ADD INDEX indexName(columnName)
    3. 创建表的时候直接指定: CREATE TABLE mytable(ID INT NOT NULL, username VARCHAR(16) NOT NULL, INDEX [indexName] (username(length)))
    4. 删除索引: DROP INDEX [indexName] ON mytable
## **`唯一索引`**
* 与普通索引不同的是, 唯一索引的索引列值必须唯一, 但允许有空值. 如果是组合索引, 则列组合值必须是唯一的, 创建方法与普通索引类似
    ## **`创建方式`**
    1. 直接创建: CREATE UNIQUE INDEX indexName ON mytable(username(length))
    2. 修改表结构的方式添加索引: ALTER table mytable ADD UNIQUE [indexName] (username(length))
    3. 创建表的时候直接指定: CREATE TABLE mytable(ID INT NOT NULL, username VARCHAR(16) NOT NULL, UNIQUE [indexName] (username(length)))
    4. 删除索引: DROP INDEX [indexName] ON mytable;
## **`组合索引`**
* 平时用的SQL查询语句一般都有比较多的限制条件, 所以为了进一步榨取MySQL的效率, 就要考虑建立组合索引. 如: ALTER TABLE table_name ADD INDEX index_key1_key2(key1(50), key2(10)). 建立这样的组合索引相当于分别建立了这样的两组索引: -key1, key2, -key1. 没有单独的key2索引是因为MySQL采用最左前缀的结果. 简单理解就是只从最左面开始组合, 并非只要包含这两列的查询都会用到该组合索引. 如SELECT * FROM table_name WHERE key1=xxx and key2=yyy 和 SELECT * FROM table_name WHERE key1=xxx都会使用到索引. 而SELECT * FROM table_name WHERE key2=yyy则不会使用到索引. 