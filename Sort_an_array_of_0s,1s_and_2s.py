#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  1 23:00:07 2017

@author: ska

Sort an array of 0s, 1s and 2s
"""

for _ in range(int(input())):
	n = int(input())
	ar = list(map(int, input().split()))
	z=0
	o=0
	t=0
	for i in ar:
		if i ==0:
			z += 1
		elif i == 1:
			o += 1
		else:
			t += 1
	s = '0 '*z+'1 '*o+'2 '*t
	print(s[:-1])