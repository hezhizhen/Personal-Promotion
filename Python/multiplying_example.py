# -*- coding: utf-8 -*-
# 在屏幕上打印一个由字符组成的“盒子”，该“盒子”在屏幕上居中并且能根据用户输入的句子自动调整大小
# 以正确的宽度在居中的“盒子”内打印一个句子
# 整数除法运算符：//

sentence = raw_input("Sentence: ")

screen_width = 80
text_width = len(sentence)
box_width = text_width+6
left_margin = (screen_width - box_width) // 2

print
print ' ' * left_margin + '+' + '-' * (box_width-2) + '+'
print ' ' * left_margin + '|  '+ ' ' * text_width    + '  |'
print ' ' * left_margin + '|  '+       sentence      + '  |'
print ' ' * left_margin + '|  '+ ' ' * text_width    + '  |'
print ' ' * left_margin + '+' + '-' * (box_width-2) + '+'

# 注意：打印的盒子中第2、3、4行竖线后和最后的竖线前分别有2个空格(that explains why box_width-2)
