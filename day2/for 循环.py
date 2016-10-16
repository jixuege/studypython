#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author: Leon xie
age=20
#注意for下面的缩进问题
for i in range(3):

    gues_age = int(input("age:"))  # str --> int

    if gues_age == age:
        print("right!!")
    elif  gues_age > age:
        print("try smaller.....")
    else:
        print("try bigger...")
else:
    exit("too many attempts....")