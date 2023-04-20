---
layout: post
title: Python
mathjax: true
categories: code
tags: Python
keywords: Python
description: Record Python knowledge points
mermaid: true
highlight: true
status: Archived
type: mdpdf
repopath: 2022-05-04-python-cn
---

莫烦Python基础

## 变量与运算

name="文件管理系统"，name 变量名，文件管理系统 变量的值

可以用双引号，单引号，和三个引号（可单可双）

三个引号的在文本量比较多的情况下有一个好处，就是可以书写**跨行**的文本

## Print

print("莫烦Python的", name, "业界顶呱呱")

## 数学运算

\+ - * / 加减乘除 3/2=1.5

注意，字符串也是可以加起来的（不能相减）

name = "文件" + "系统"

% 取模  103%100=3

\** 幂  3**2=9

// 取整除  10//3=3

a = 1
a += 1

a=2

## 条件判断

### if 如果

if

if-else

if-elif-else

### for循环

for i in range(5):
    print("新文件-" + str(i))

i=0,1,2,3,4 取不到5

range(3,10,2)  3,5,7,9       2是step

### while循环

|       | 特点          |
| ----- | ----------- |
| for   | 天然适合在有限的循环中 |
| while | 可以被用在无限循环中  |

|          | 比喻   |
| -------- | ---- |
| break    | 中断循环 |
| continue | 继续循环 |

## 

## List 列表 []

files = ["f1.txt", "f2.txt", "f3.txt", "f4.txt", "f5.txt"]

files[0]  f1.txt

files[-1]  f5.txt

files[-3:]  ['f3.txt', 'f4.txt', 'f5.txt']

files[1] = 12  f2.txt->12  修改列表的值

在列表中，你可以存放**不同类型的元素**，字符，数字，甚至列表里还能有列表。

l = [1, "file", ["2", 3.2]]
print(l)
l[2][0] = "new string"
print(l)

[1, 'file', ['2', 3.2]]  
[1, 'file', ['new string', 3.2]]

## Dict 字典 {} key-value

files = {"ID": 111, "passport": "my passport", "books": [1,2,3]}

print(files[books])

files["ID"]=222  通过key修改对应的value

注意哦，在字典中的元素不像列表，**字典元素是没有顺序的**

## 元组 ()

files = ("file1", "file2", "file3")

元组的值不可以改变

## Set 集合 {}

set 里面只会存在非重复的元素，注意哦，在集合中的元素，其实是**没有顺序**的。

my_files = set(["file1", "file2", "file3"])

your_files = {"file1", "file3", "file5"}

### 在循环中运用

files = ["f1.txt", "f2.txt", "f3.txt", "f4.txt", "f5.txt"]

for i in range(**len**(files)):

for f in **files**:

取字典的key和value `dict.items()`, `dict.keys()`, `dict.values()`

列表添加和pop  .append  .pop（从最后一个pop值）



Python 在列表，元组，字典变量前加\*号
