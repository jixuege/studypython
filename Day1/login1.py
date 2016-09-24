#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author: Leon xie

import getpass
name = input("输入用户：")
pwd = getpass.getpass("请输入密码：")

if name == "xiedi" and pwd =="123":
    print("登陆成功")
else:
    print("登陆失败")

