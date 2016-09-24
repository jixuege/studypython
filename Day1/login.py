#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author: Leon xie

name = input("请输入用户名：")  #输入xiedi
"""
if name == "xiedi":    #值对比，不是内存地址对比
    print("登陆成功")
else:
    print("登陆失败")

#if 里面加了条件，如果成功，执行第一个，否则，else下的代码执行
#赋值的时候是1个等号，比较的时候是2个等号，
"""

if name == "eric":
    print("普通")
elif name =="tory":
    print("超级")
elif name =="alex":
    print("超神")
else:
    print("非法")