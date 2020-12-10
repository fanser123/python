# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
'''
对象的比较
'''
# x = 1
# y = 1
# print(id(x), id(y))
# print(x is y)  # false
#
# x = [1, 3 ,5 ]
# y = [1, 3 ,5 ]
#
# print(x is not  y) # is 内存地址
#
# print( x == y) # 比较内容

x=1
y=1
print(id(x),id(y))
print(x is y)
x=[1,3,5]
y=[1,3,5]
print(x is not y)
print(x==y)