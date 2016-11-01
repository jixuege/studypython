#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author: Leon xie

msg='hello world'

print(msg.capitalize())
print(msg.center(20))
print(msg.center(20,'#'))
print(msg.count('l'))
print(msg.endswith('1'))

msg1='a\tb'
print(msg1.expandtabs(10))
print(msg1)

print('{0} {1} {0}'.format('name','age'))
print('{name}'.format(name='xiedi'))

print('{} {}').format('name','age')

