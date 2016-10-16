#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author: Leon xie


username = "xiedi"
password = "123"

user = input("用户名：")
passwd = input("密码：")

if user == username and passwd == password:
    print("welcome to login.....")
else:
    print("登录失败")


#打开一个文件，用于写入，后面的'wb'表示每次写入前格式化文本，如果此文件不存在，则创建一个此文件名的文件
f2 = open('heimingdan.txt','wb')
for x in
