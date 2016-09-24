#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author: Leon xie


def author(func):
    def inner():
        print("认证")
        func()
    return inner

@author
def f1():
    print("hehe")
