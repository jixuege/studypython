#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author: Leon xie

import getpass

name = input("请输入用户名：")
pwd = getpass.getpass("请输入密码：")

if pwd == "123":
    if name == "alex":
        print("Alex。超神")
    elif name == "tory":
        print("tory,普通")
    else:
        print("登陆失败")
else:
    print("登陆失败")
