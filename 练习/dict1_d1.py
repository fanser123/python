# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
'''
增加一项， gender  : 男
修改 2项 ， 学生编号 -》 002  学生名字 --》 甘露
删除gradeid项，并返回数据
'''
#字典
stu = {
    "studentNo": "001",
    "studentName": "陈超",
    "phone": "1212312",
    "address": "武汉",
    "bornDate": "2020/9/8",
    "gradeId": 3
}
stu["gradeId"]="4"
stu['gender']="男"
print(stu)
stu.update({
    "gender":"男",
    "studentNo":"002",
    "studentName":"甘露"
})
value=stu.pop("gradeId")
print(value)
dict()
# r=stu.items()
# print(r)
# for k,v in r :
#     print("key == {},value=={}".format(k,v))
for k,v in stu.items():
    print("key=={},value={}".format(k,v))
print("\n")
for k in stu.keys():
    print("人物说明：{}".format(k))
print("\n")
for v in stu.values():
    print("人物的基本信息：{}".format(v))

