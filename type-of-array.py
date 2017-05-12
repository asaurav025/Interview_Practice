#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 12:10:52 2017

@author: ska

type-of-array:BASIC
"""
for _ in range(int(input())):
	n =int(input())
	ar = list(map(int, input().split()))
	f1 = True
	f2 = 0
	c1 = 0
	c2 =0
	for j in range(n-1):
		if ar[j] >ar[j+1]:
			c1 +=1
		else:
			c2 +=1
	if c2>c1:
		if c1 >0:
			print(max(ar), 4 )
		else:
			print(max(ar), 1)
	else:
		if c2>0:
			print(max(ar), 3)
		else:
			print(max(ar), 2)
#==============================================================================
# 	if ar[0]>ar[1]:
# 		f1 =False#decending
# 	for i in range(n-1):
# 		if ar[i] > ar[i+1] and f1:
# 			f2  = 1#accending rotated
# 			break
# 		if ar[i] <ar[i+1] and not f1:
# 			f2 = -1 #decending rotated
# 			break
# 	if f2 == 0:
# 		if f1:
# 			print(max(ar), 1)
# 		else:
# 			print(max(ar), 2)
# 	else:
# 		if f1:
# 			print(max(ar), 4)
# 		else:
# 			print(max(ar),3)
#==============================================================================
