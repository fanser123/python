#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang
'''
返回多个值

'''
def  foo1():

    return  1, 3 , 4

if __name__ == '__main__':

    x = foo1()

    print(x)
    pass

x=1
s="%04d"%x
print(s)
a=[1,3,5,7]
a.insert(3,1)
print(a[1:])