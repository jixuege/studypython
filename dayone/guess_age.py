#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author: Leon xie

# guess ages games
age = 20

gues_age = int(input("age:"))  # str --> int
print(type(gues_age))
if gues_age == age:
    print("right!!")
elif  gues_age > age:
    print("try smaller.....")
else:
    print("try bigger...")