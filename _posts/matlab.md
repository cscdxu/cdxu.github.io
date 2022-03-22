---
layout: post
title: 李群和李群的李代数
mathjax: true
categories: Topology Lie-group
tags: Lie-algebra Lie-group
keywords: Lie-algebra Lie-group
description: My understanding of Lie-group and its Lie-algebra. The statement "Lie-algebra is approximation of Lie-group" is inaccurate since they essentially live in different spaces. This post is not finished. Check posts under [`Lie Group`](https://yk-liu.github.io/blog/tags#Lie-group) and/or [`Lie Algebra`](https://yk-liu.github.io/blog/tags#lie-algebra) where I rewrote and added more aspects of Lie group and Lie algebra.
mermaid: true
highlight: true
status: Archived
---

1.清空：输入“clc”加回车，清空。

				“clear all”清空工作区。 

   注释：“%% ”-横线和横线之间的注释

  			 “%”——普通注释 

2.变量名：1）区分大小写  2)变量名以字母开头，可以由数字、字母、下划线组成，但不能使用标点。

3.脚本命名最好也以字母开头巴拉巴拉（和变量名遵循相同的规则）

4.数据类型：1）数字

2）字符和字符串（单引号）

3）矩阵！

a.  A=[1 2 3;4 5 2; 3 2 7; 2 3 4]

​	A' 转置；A(:)竖着拉长，成一列；

​	inv(A) 逆矩阵

b.rand,randn,randi

4) 元胞数组

   A=cell（1，6） (matlab的数组是从1开始的！！）

   A{2}=eye（3） eye（3）——生成一个3*3的对角单位矩阵

 A{5}=magic（5）生成5阶幻方（横竖斜数字之和总相等）

5）.结构体

  books=struct(‘name’,{{'hhh','qqq'}},'price',[30,40])

  books.name(1)-取出的是cell（有单引号）

  books.name{1}-取出的是字符串（无，，，）

5.矩阵操作

A=a: b : c （a,区间起点；c，区间终点；b：步长）

B=repmat（A，3，2）

C=ones（2，4（生成的矩阵里每个数字都是1）

矩阵的四则运算

  F=A.*B  (对应数字相乘）

  G=A/B(A乘以B的逆）

  H=A./B（对应数字相除）

矩阵的下标（起始是1而不是0）

  A=magic（5）

  B=A（2，3）  B=A（：，3）

 [m,n]=find(A>20)



###### 循环结构

```
sum = 0;
for n = 1:5
	sum = sum + n^2;
end
```

![image-20220322100345084](C:\Users\xcd\AppData\Roaming\Typora\typora-user-images\image-20220322100345084.png)

```
s = 0;
n = 1;
while n<= 10
	s = s + n;
	n = n + 1;
end
```

![image-20220322101129144](C:\Users\xcd\AppData\Roaming\Typora\typora-user-images\image-20220322101129144.png)



###### 分支结构

![image-20220322101601369](C:\Users\xcd\AppData\Roaming\Typora\typora-user-images\image-20220322101601369.png)



![image-20220322101814584](C:\Users\xcd\AppData\Roaming\Typora\typora-user-images\image-20220322101814584.png)



#### 绘图

线条颜色、线型、数据标记点
