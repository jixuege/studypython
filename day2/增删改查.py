#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author: Leon xie

name = ["jixuege","dajiba","boduoye","cangjinkong","youtianai"]
print(name[-1])
print(name[:2])
print(name[0],name[1])
n1=name.copy()
print(name)
print(n1)

n2=name.pop()
print(n2)

name = ["jixuege","dajiba","boduoye","cangjinkong","youtianai"]

name.insert(2,"youhua")
print(name)

#删
name.remove("youhua")
del name[3]
print(name.pop())
print(name)

#改
name = ["jixuege","dajiba","boduoye","cangjinkong","youtianai"]
name[2]="wuming"
print(name)

name = ["jixuege","dajiba","boduoye","cangjinkong","youtianai"]
name.pop(1)
print(name)














