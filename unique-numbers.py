#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 11:53:05 2017

@author: ska
unique-numbers:BASIC

"""
for _ in range(int(input())):
	m,n = map(int, input().split())
	ar = []
	for i in range(m,n+1):
		a = str(i)
		if len(a) == len(set(a)):
			ar.append(a)
			
	print(" ".join(ar))