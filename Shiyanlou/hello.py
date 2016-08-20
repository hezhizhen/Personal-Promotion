#!/usr/bin/env python
#coding=utf-8
# chmod 755 hello.py 脚本
print('Hello World!')
print('-'*50)

a = 10
print(a, type(a)) # type()可查询变量的类型
print('-'*50)

s1 = (2, 1.3, 'love', 5.6, 9, 12, False) # tuple
s2 = [True, 5, 'smile'] # list
print(s1,type(s1))
print(s2,type(s2))
print('-'*50)

s3 = [1, [3,4,5]]
print(s3[1][2])
print('-'*50)

# 范围引用的基本样式：[下限：上限：步长]，其中下限的元素包括，上限的元素不包括，步长默认为1
print(s1[:5]) # 从开售到下标为4（最后一个元素不包括）
print(s1[2:]) # 从下标2到最后
print(s1[0:5:2]) # 从下标0到下标4，隔一个取一个元素
print(s1[2:0:-1]) # 从下标2到下标1
print(s1[0:-1]) # -1为最后一个元素，即不包括最后一个元素
print('-'*50)

strs = 'abcdef' # 字符串是tuple

print(10%3) # 取余
print('-'*50)

# 数学运算：+ - * / ** %
# 判断：== !- < <= > >= in is is not
# 逻辑：and or not

i = 1
x = 1
if i>0:
    x += 1
elif i==0:
    pass
else:
    pass
print(x)
print('-'*50)

for a in [3,4.4,'life']:
    print(a)
print('-'*50)

idx = range(5) # range()新建list，元素都是整数，从0开始，步长为1，直到上限为参数（上限不包括）
print(idx)

for a in range(10):
    print(a**2)
print('-'*50)

i = 0
while i<10:
    print(i)
    i += 1
print('-'*50)

# continue 和 break 同C++中的一样

# 函数
def square_sum(a,b):
    c = a**2 + b**2
    return c # return可以返回多值，以逗号分隔，相当于返回tuple。没有return或者return后面没有返回值时，函数返回None
print(square_sum(3,4))
print('-'*50)

a = 1
def change_integer(a):
    a += 1
    return a
print(change_integer(a)) # 原整数没有改变。 值传递
print(a)
print('-'*50)

b = [1,2,3]
def change_list(b):
    b[0] += 1
    return b
print(change_list(b)) # 原list发生改变。 指针传递
print(b)
print('-'*50)

class Bird(object): # 对象 object说明这个类没有父类
    have_feather = True # 属性
    way_of_reproduction = 'egg'
    def move(self, dx, dy): # 方法 self为了方便引用对象自身，第一参数必须是self
        position = [0,0]
        position[0] += dx
        position[1] += dy
        return position

summer = Bird()
print(summer.way_of_reproduction)
print('after move:',summer.move(5,8))
print('-'*50)

class Chicken(Bird): # 子类，继承
    way_of_move = 'walk'
    possible_in_KFC = True

class Oriole(Bird):
    way_of_move = 'fly'
    possible_in_KFC = False

summer = Chicken()
print(summer.have_feather)
print(summer.move(5,8))
print('-'*50)

class Human(object):
    laugh = 'hahahaha'
    def show_laugh(self):
        print(self.laugh)
    def laugh_10th(self):
        for i in range(10):
            self.show_laugh()

li_lei = Human()
li_lei.laugh_10th()
print('-'*50)

# __init__()是特殊方法，前后各两下划线，初始化
class happyBird(Bird):
    def __init__(self, more_words):
        print('We are happy birds.', more_words)

summer = happyBird('Happy, Happy!')
print('-'*50)

class Human(object):
    def __init__(self, input_gender):
        self.gender = input_gender
    def printGender(self):
        print(self.gender)
lilei = Human('male') # gender不是类属性，是对象属性 lilei.gender
print(lilei.gender)
lilei.printGender()
print('-'*50)

print(dir(list)) # dir()查询一个类或者对象所有属性
# print(help(list)) # help()查询说明文档
print('-'*50)

# list的一些方法
nl = [1,2,5,3,5]
print(nl.count(5)) # 统计5的次数
print(nl.index(3)) # 查询第一个3的下标
nl.append(6) # 最后添加新元素6
nl.sort() # 排序
print(nl)
print(nl.pop()) # 去除最后一个元素，并返回该元素
nl.remove(2) # 去除第一个2
nl.insert(0,9) # 在下标为0处插入9
print(nl)
print('-'*50)

print([1,2,3]+[5,6,9]) # +运算符
class superList(list):
    def __sub__(self,b):
        a = self[:]
        b = b[:]
        while len(b)>0:
            element_b = b.pop()
            if element_b in a:
                a.remove(element_b)
        return a
print(superList([1,2,3]) - superList([3,4]))
print('-'*50)

# 闰年
class years(object):
    year = 0000
    month = 0
    day = 0
    def __init__(self,a,b,c):
        self.year = a
        self.month = b
        self.day = c
    def judge(self):
        if self.year%4 != 0:
            return False
        elif self.year%100==0 and self.year%400!=0:
            return False
        else:
            return True

test = years(2004,1,1)
print(test.judge())
print('-'*50)

# 容器：存储多个元素的对象
dic = {'tom':11, 'sam':57, 'lily':100} # dict: key & value 字符串来表示key，或数字和真值 key不可变。 dict的元素没有顺序
print(type(dic))
print(dic['tom']) # 通过key来引用元素
dic = {} # blank dict
print(dic)
dic['lilei'] = 99 # 添加元素至dict
print(dic)
dic = {'lilei': 90, 'lily': 100, 'sam': 57, 'tom': 90}
for key in dic:
    print(dic[key])

print(dic.keys()) # 返回所有的key
print(dic.values()) # 返回所有的value
print(dic.items()) # 返回所有key-value对
del dic['tom'] # 删除某元素
print(dic)
print(len(dic))
dic.clear() # 清空dict
print(dic)
print('-'*50)

# 文件输入输出
# 对象名 = open(文件名，模式)
# 模式有：r, r+, w, w+, a, a+。 r系列文件必须存在，w系列若文件存在则清空内容，若文件不存在则建立，a系列若文件不存在则建立，若存在则附加至文件尾。 +为可读写
# b字符表示打开的文件为二进制文件，非纯文字文件
f = open("test.txt","r+")
content = f.read(10) # 读取10 bites的数据
print(content)
content = f.readline() # 读取一行
print(content)
content = f.readlines() # 读取所有行
print(content)
f.write('I like apple!\n')
f.close() # 关闭文件
print('-'*50)

# 模块， 写在最前面
# import a as b 引入模块a，并将模块a重命名为b
# from a import function1 从模块a中引入function1对象。调用时直接使用function1而非a.function1
# from a import * 从模块a中引入所有对象，调用时直接使用对象
# 搜索路径：程序所在文件夹，环境变量包含路径，标准库安装路径
# 模块包：可以把功能相似的模块放在同一个文件夹中，该文件夹中须包含一个__init__.py文件，可以为空文件
# import this_dir.module 引入this_dir文件中的module模块

# 参数传递
# 位置传递：根据参数的位置传递参数，如f(1,2,3)
# 关键字传递：根据参数的名字传递参数，如f(c=3,b=2,a=1)
# 上述两种传递方式可以混用
# 函数可以给参数赋予默认值，如def f(a,b,c=10)，调用时可以为f(3,2)或f(3,2,1)
# 包裹传递：不清楚参数个数时。
# 包裹位置传递：如def func(*name)，调用时f(1,4,6)和f(1,2,3,4,5,6,7)都是可行的
# 包裹关键字传递：如def func(**dict)，调用时func(a=1,b=9)
# 解包裹：调用时先定义tuple，再用tuple作参数，如def func(a,b,c)，调用时args=(1,2,3), func(*args)；dict = {'a':1,'b':2}, func(**dict)

s = 'abcdefghijk'
for i in range(0,len(s),2): # range(上限，下限，步长)
    print(s[i])
print('-'*50)

for (index, char) in enumerate(s): # enumerate()返回一个两个元素的tuple
    print (index, char)
print('-'*50)

ta = [1,2,3]
tb = [9,8,7]
tc = ['a','b','c']
for (a,b,c) in zip(ta,tb,tc): # zip()从各个序列各取一个元素合成一个tuple，各序列需等长
    print(a,b,c)
print('-'*50)

# cluster
zipped = zip(ta,tb)
print(zipped)
# decompose
na, nb = zip(*zipped)
print(na,nb)
print('-'*50)

# 循环对象包含next()方法，直到StopIteration错误
# iter()函数
# 生成器，类似函数，只是return改成yield。可以有多个yield
def gen():
    a = 100
    yield a
    a += 8
    yield a
    yield 1000

for i in gen():
    print i

def gen():
    for i in range(4):
        yield i
G = (x for x in range(4))
print(G)
print('-'*50)

# 表推导：快速生成表的方法
L = []
for x in range(10):
    L.append(x**2)
print(L)
L = [x**2 for x in range(10)]
print(L)
print('-'*50)

# lambda函数
func = lambda x,y:x+y
print(func(3,4))

# 函数作为参数传递
def test(f,a,b):
    print('test')
    print(f(a,b))
test(func,3,5)
test((lambda x,y:x**2+y),6,9)
print('-'*50)

# map()
re = map((lambda x:x+3),[1,3,5,6]) # 2个参数，第1个参数为函数，第二个参数为表。功能是将函数对象依次作用于表的每一个元素
print(re)

# filter()函数
def func(a):
    if a>100:
        return True
    else:
        return False
print(filter(func,[10,56,101,500])) # 如果函数对象返回True，则该次的元素被存储于返回的表中

# reduce()
print(reduce((lambda x,y:x+y),[1,2,5,7,9])) # reduce()的第一个参数的函数只能接收2个参数，累进作用于各个参数
print('-'*50)

re = iter(range(5))
try: # 在try中放入容易犯错的部分
    for i in range(100):
        print(re.next())
except StopIteration:
    print('Here is end ', i)
print('hahahaha')

def test_func():
    try:
        m = 1/0
    except NameError:
        print('Catch NameError in the sub-function')
try:
    test_func()
except ZeroDivisionError:
    print('Catch error in the main program')
print('-'*50)

# 抛出异常
print('lalala')
# raise StopIteration
print('hahaha')
print('-'*50)

# C语言中的变量即Python中的对象。对象是存储在内存中的实体，并不能直接接触，对象名只是指向该对象的引用
# 引用和对象分离，是动态类型的核心
a = 3
print(a)
a = 'at'
print(a)

L1 = [1,2,3]
L2 = L1
L1[0] = 10
print(L2) # L1和L2指向同一个表
print('-'*50)

# 函数的参数传递，本质上传递的是引用
# 不可变数据对象，值传递

# 特殊方法：前后各俩下划线
# 运算符是通过调用对象的特殊方法实现的
print('abc'+'xyz')
print('abc'.__add__('xyz')) # 实际上是这样实现加法的

# 内置函数也调用对象的特殊方法
print(len([1,2,3]))
print([1,2,3].__len__())

# 表元素的引用
li = [1,2,3,4,5,6]
print(li[3])
print(li.__getitem__(3))

# 函数也是一种对象。任何一个有__call__()特殊方法的对象都是函数
class SampleMore(object):
    def __call__(self,a):
        return a+5
add = SampleMore() # 一个函数对象
print(add(2)) # 函数调用
print(map(add,[2,4,5]))
print('-'*50)

# 上下文管理器
# 可以在不需要文件时，自动关闭文件
f = open('test.txt', 'w')
print(f.closed)
f.close()
print(f.closed)

with open('test.txt','w') as f:
    print(f.closed)
print(f.closed) # 退出with as程序块后自动关闭文件

# 任何定义了__enter__()和__exit__()方法的对象都可以用于上下文管理器
# 文件对象是内置对象，自带俩特殊方法
class VOW(object):
    def __init__(self, text):
        self.text = text
    def __enter__(self):
        self.text = 'I say: ' + self.text
        return self
    def __exit__(self, exc_type, exc_value,traceback):
        self.text = self.text + '!'

with VOW("I'm fine") as myvow:
    print(myvow.text)
print(myvow.text)
print('-'*50)

# 每个对象可以有多个属性，对象的属性存储在对象的__dict__属性中，key为属性名，value为属性本身
