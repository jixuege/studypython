#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author: Leon xie

import getpass


name = input("请输入用户名：")
pwd = getpass.getpass("请输入密码：")

if name == "alex" and pwd == "cmd":
    print("欢迎，alex!")
else:
    print("用户名和密码错误！")