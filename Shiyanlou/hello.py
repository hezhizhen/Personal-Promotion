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
print(help(list)) # help()查询说明文档
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
