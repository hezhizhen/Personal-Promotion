#! /usr/bin/env python
# -*- coding: utf-8 -*-
# normal division
# from __future__ import division
import math
import cmath
from math import sqrt

# Start
print "hello world"

# Numbers & Expressions
2+2
1/2
1.0/2.0
1//2 # 整除
1.0//2.0
10%3 # 取余
2**3 # 乘方
1000000000000000000000000000 # long int
0xAF # 十六进制
010 # 八进制

# Variables
x=2 # 赋值
x*3

# Sentences
2*2 # 表达式
print 2*2 # 语句（print语句）
x=3 # 赋值语句

# Input
input("The meaning of life: ") # 打印字符串并接受输入数字

x=input("x: ")
print x**2

if 1==2: print "One equals two" # if语句（注意冒号）
if 1==1: print "One equals one"

# Functions
pow(2,3) # 2**3
pow(2,3*5)
abs(-10)
round(1.0/2.0) # 把浮点数四舍五入为最接近的整数
round(1/2)
# floor 向下取整

# Modules
# math
print math.floor(32.9) # 向下取整
int(32.0)
print math.ceil(32.3) # 向上取整
print sqrt(4)
print math.sqrt(9)
print cmath.sqrt(-1)
(1+3j)*(9+4j) # 复数

name=raw_input("What is your name? ")
print "Hello, " + name + "!" # 以+连接
raw_input("Press <enter>")

x="hello "
y="world"
x+y

print repr("hello world")
print str("hello world")
print ("hello world")

print ''' this is a very long
long
long
long
long
sentence.'''
print "hello \
world"

print r"C:\nowhere" # 原始字符串
print u"hello world" # Unicode字符串

edward = ['Edward Gumby', 42]
john = ['John Smith', 50]
database = [edward, john]
print database

# index
greeting="hello"
print greeting[0]
print greeting[-1]

print 'Hello'[1]

fourth = raw_input("Year: ")[3]
print fourth

# slicing
numbers=[1,2,3,4,5,6,7,8,9,10]
print numbers[3:6]
print numbers[0:1]
print numbers[5:-3]
print numbers[7:10] # 索引10指向第11个元素，该元素不存在
print numbers[-3:]
print numbers[:3]
print numbers[:] # 打印所有元素
print numbers[0:10:2] # 步长为2
print numbers[8:3:-1] # 步长为负数

print [1,2,3]+[4,5,6] # 序列相加
print 'python'*5

emptys = []
print emptys
sequence = [None]*10
print sequence

# in
permissions = 'rw'
print 'w' in permissions
print 'x' in permissions

users = ['mlh', 'foo', 'bar']
print raw_input('Enter your name: ') in users

# built-in function len&max&min
numbers = [100,34,678]
print len(numbers)
print max(numbers)
print min(numbers)
print max(1,2,3,4,5)

# list
print list('Hello')
xs=[1,1,1]
xs[1]=2
print xs
del xs[2]
print xs

name=list('Perl')
name[1:]=list('ython')
print name

numbers = [1,5]
numbers[1:1] = [2,3,4]
print numbers # 用分片赋值实现插入

numbers[1:4] = []
print numbers # 用分片赋值实现

# append
numbers.append(6)
print numbers

# count
x=[[1,2],1,1,[2,1,[1,2]]]
print x.count(1)

# extend
a=[1,2,3]
b=[4,5,6]
a.extend(b)
print a

# index
knight=['We','are','the','knights','who','say','ni']
print knight.index('who')

# insert
numbers=[1,2,3,5,6,7]
numbers.insert(3,'four')
print numbers

# pop
x=[1,2,3]
print x.pop()
print x
print x.pop(0)

# remove
x=['to','be','or','not','to','be']
print x.remove('be')
print x

# reverse
x=[1,2,3]
x.reverse()
print x

# sort
x=[5,4,3,2,1]
y=x[:] # 通过分片赋值来复制列表
y.sort()
print x
print y

y=sorted(x) # y指向已排序的x的列表的副本，并不是复制
print x
print y

# cmp
print cmp(42,32)
print cmp(99,100)
numbers=[5,2,9,7]
numbers.sort(cmp)
print numbers

x=['aardvark', 'abalone', 'acme', 'add', 'aerate']
x.sort(key=len)
print x
x=[1,2,3,4,5]
x.sort(reverse=True)
print x
