#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author: Leon xie

pangzi_age= 22
count = 0
while count <3:
    guess_age = input("age:")
    if guess_age.isdigit():
        guess_age=int(guess_age)
    else:
        continue
    if guess_age >22:
        print("guess big")
    elif  guess_age == 22:
        print("guess right")
        break
    else:
        print("guess smaller")

    count +=1
