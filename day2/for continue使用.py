#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author: Leon xie

for i in range(10):
    for j in range(10):
        if j < 5:
            #break   #跳出整个当前循环，跳出这一层
            continue # 跳出当次循环，继续下一次循环
        print(i,j)