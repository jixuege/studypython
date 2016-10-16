#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author: Leon xie

score = int(input("输入你的成绩："))
if score >100:
    print("error")
elif score == 100:
    print("A+")
elif score >=90:
    print("A")
elif score >=80:
    print("B")
elif score >=60:
    print("C")
elif score >=40:
    print("C-")
else:
    print("D")

# if匹配，可以匹配多个，但是只匹配一项，从上往下走，遇到匹配就执行。