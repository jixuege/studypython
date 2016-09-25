#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author: Leon xie


"""
print(input("name:"))
print(input("age:"))
"""
"""
name = input("name:")
age = input("age:")
job = input("job:")
hobby = input("hobby:")
print(name)
print(age)
print(job)
print(hobby)

"""

# 传变量
name = input("name:")
age = input("age:")
job = input("job:")
hobby = input("hobby:")

#print("my name is",name,"i am",age,"years old,\n"

#        "my job is",job,"my hobby is",hobby)

# 占位符

info = '''
-----info of %s--------
Name: %s
Age: %s
Job: %s
Hobby: %s
----------end-------------

'''  %(name,name,age,job,hobby)

print(info)









