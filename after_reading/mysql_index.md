### [MySQL索引创建及使用](https://blog.csdn.net/dengchenrong/article/details/88425762)

## **`MySQL索引概念`**
* 索引是一种特殊的文件(InnoDB数据表上的索引是表空间的一个组成部分), 它们包含着对数据表里所有记录的引用指针. 更通俗的说, 数据库索引好比是一本书前面的目录, 能加快数据库的查询速度. 有了相应的索引之后, 数据库会直接在索引中查找符合条件的选项. 索引分为聚集索引和非聚集索引, 聚集索引指的是数据行的物理顺序与列值(一般是主键的那一列)的逻辑顺序相同, 一个表中只能拥有一个聚集索引. 除了聚集索引以外的索引都是非聚集索引, 非聚集索引中索引的逻辑顺序与磁盘上行的物理存储顺序不同，一个表中可以拥有多个非聚集索引

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
* 平时用的SQL查询语句一般都有比较多的限制条件, 所以为了进一步榨取MySQL的效率, 就要考虑建立组合索引. 如: ALTER TABLE table_name ADD INDEX index_key1_key2(key1(50), key2(10)). 建立这样的组合索引相当于分别建立了这样的两组索引: -key1, key2, -key1. 没有单独的key2索引是因为MySQL采用最左前缀的结果. 简单理解就是只从最左面开始组合, 并非只要包含这两列的查询都会用到该组合索引. 如SELECT * FROM table_name WHERE key1=xxx and key2=yyy 和 SELECT * FROM table_name WHERE key1=xxx都会使用到索引. 而SELECT * FROM table_name WHERE key2=yyy则不会使用到索引

## **`索引的优化`**
* 虽然索引大大提高了查询速度, 同时却会降低更新表的速度, 如对表进行INSERT, UPDATE和DELETE. 因为更新表时, MySQL不仅要保存数据, 还要保存一下索引文件. 建立索引会占用磁盘空间的索引文件. 一般情况这个问题不太严重, 但如果你在一个大表上创建了多种组合索引, 索引文件的会膨胀很快. 索引只是提高效率的一个因素, 如果你的MySQL有大数据量的表, 就需要花时间研究建立最优秀的索引, 或优化查询语句
1. 索引不会包含有NULL值的列: 只要列中包含有NULL值都将不会被包含在索引中, 复合索引中只要有一列含有NULL值, 那么这一列对于此复合索引就是无效的. 所以在数据库设计时不要让字段的默认值为NULL
2. 使用短索引: 对串列进行索引, 如果可能应该指定一个前缀长度. 例如, 如果有一个CHAR(255)的列, 如果在前10个或20个字符内, 多数值是惟一的, 那么就不要对整个列进行索引. 短索引不仅可以提高查询速度而且可以节省磁盘空间和I/O操作
3. 索引列排序: MySQL查询只使用一个索引, 因此如果WHERE子句中已经使用了索引的话, 那么order by中的列是不会使用索引的. 因此数据库默认排序可以符合要求的情况下不要使用排序操作. 尽量不要包含多个列的排序, 如果需要最好给这些列创建复合索引
4. LIKE语句操作: 一般情况下不鼓励使用LIKE操作, 如果非使用不可, 如何使用也是一个问题. LIKE "%aaa%" 不会使用索引而LIKE "aaa%" 可以使用索引
5. 不要在列上进行运算: SELECT * FROM users WHERE YEAR(adddate) < 2007, 将在每个行上进行运算, 这将导致索引失效而进行全表扫描, 因此我们可以改成: SELECT * FROM users WHERE adddate < '2007-01-01'
6. MySQL只对以下操作符才使用索引: <, <=, =, >, >=, BETWEEN, IN, 以及某些时候的LIKE(不以通配符 % 或 _ 开头的情形)