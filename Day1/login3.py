#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author: Leon xie

NAME = "xiedi"
PASSWD = "123"

name = input("请输入用户名：")
pwd = input("请输入密码：")

if NAME == name and PASSWD == pwd:
    print("welcome,%s" % NAME)
else:
    print("error")