#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author: Leon xie

#定义商品列表元素
products= [
    ["Iphone",5800],
    ["Mac",15800],
    ["Coffee",30]
]

#定义一个购物车空列表
products_list=[ ]
salary = input("请输入你的工资：")
#加入到while循环进行重复输入
while True:
    #salary = input("请输入你的工资：")

  #  choice_numb=input(">>")
#打印商品列表
    for i,ele in enumerate(products):
        print(i,ele[0],ele[1])
    choice_numb=input(">>")
    #判断输入字符是否为数字
    if choice_numb.isdigit():
        choice_numb=int(choice_numb)
    else:
        print("请输入小于3的数字")
        continue
    if choice_numb >2:
        print("请输入小于3的数字")
    if choice_numb == 0:
        if int(salary) >5800:
            print("get it")
            products_list=products_list.append("Iphone")
            print(products_list)
            salary = int(salary)-5800
            print("已经购买了，还剩%s"% salary)
        else:
            print("钱不够")
            print(products_list)
    if choice_numb == 1:
        if int(salary) >15800:
            print("get it")
            products_list=products_list.append(products[1][0])

            salary = int(salary)-15800
            print("已经购买了，还剩%s"% salary)
        else:
            print("钱不够")
            print(products_list)
    if choice_numb == 2:
        if int(salary) >30:
            print("get it")
            products_list=products_list.append(products[2][0])

            salary = int(salary)-30
            print("已经购买了，还剩%s"% salary)
        else:
            print("钱不够")
            print(products_list)

