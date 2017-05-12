#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 11:47:54 2017

@author: ska
geek-and-coffee-shop:BASIC
"""

for i in range(int(input())):
	n,m = map(int, input().split())
	
	while m>1:
		n = n//2
		m -= 1
	print(n)