#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  2.py
#  
#  Copyright 2018 Omer Dan <omerd@localhost.localdomain>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

longer = ' '
shorter = ' '
str1 = input('please insert string1: ')
str2 = input('please insert string2: ')
num1 = int(input('please insert number: ')

if len(str1) > len(str2):
	longer=str1
	shorter=str2
	else:
		longer=str2
		shorter=str1
print(longer)

if (str1 in str2) or (str2 in str1):
	print(str1 + ' contains ' + str2)
str3=longer[0:num1]
str4=shorter[0]
str4Fixed=longer.replace('Alex' ,str4)
str5=str1+str2+str3
print(str5.count("A"))
