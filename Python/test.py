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
