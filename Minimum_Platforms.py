#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  1 22:43:56 2017

@author: ska

Minimum Platforms
"""

for _ in range(int(input())):
	n = int(input())
	ar = [(i,1) for i in map(int,input().split())]
	de = [(i,-1) for i in map(int, input().split())]
	l =ar+de
	l.sort()
	t= 0
	m=0
	for i in range(len(l)):
		t += l[i][1]
		if t>m:
			m= t
	if m ==0:
		print(1)#because when we sort the array tuple with -1 comes first when the 1st
				#element of tuple is same so when ever there is two elemnt with same value
				#then -1 is added before +1
		continue		
	print(m)