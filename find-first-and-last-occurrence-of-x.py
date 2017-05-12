#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 12:32:37 2017

@author: ska

find-first-and-last-occurrence-of-x:BASIC
"""
for _ in range(int(input())):
	n = int(input())
	ar = list(map(int, input().split()))
	k = int(input())
	
	ab = list(reversed(ar))
	try:
		print(ar.index(k), n-ab.index(k)-1)
	except ValueError:
		print(-1)
		