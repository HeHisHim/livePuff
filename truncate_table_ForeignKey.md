### [清除具有外键约束的表](https://blog.csdn.net/weixin_40050532/article/details/80434427)s

* 当表具有外键约束时调用TRUNCATE或者DELETE, 会报错Cannot truncate a table referenced in a foreign key constraint

### 解决方法
#### 1. SET FOREIGN_KEY_CHECKS=0; -- 解除外键约束
#### 2. TRUNCATE your_table; / DELETE FROM your_table; -- 执行删除
#### 3. SET FOREIGN_KEY_CHECKS=1; -- 设置外键约束
