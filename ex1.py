#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test.py
#  
#  Copyright 2018 Omer Dan <omerd@localhost.localdomain>
#2 numbers from user

num = int(input("select a number:"))
num2 = int(input("select another number:"))

#mathematics operations
sum = num + num2
multiply = num * num2
divide = num / num2

#sum of results

print("the sum of the numbers is %s" % sum)
print("the multiply of the numbers is %s" % multiply)
print("the divide of the numbers is %s" % divide)

#check if 2 numbers are equal
if num == num2:
	print("numbers are equal")
elif num > num2:
	print("%s is bigger" % num)
elif num < num2:
	print("%s is bigger" % num2)
