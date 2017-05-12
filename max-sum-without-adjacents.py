#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  1 21:40:29 2017

@author: ska

max-sum-without-adjacents
"""
for _ in range(int(input())):
	n = int(input())
	ar =list(map(int, input().split()))
#==============================================================================
# 	now we transverse every element one by one and claculate whether the element
# 	should be present in in max sum without adjancent elements in array
#==============================================================================
	#if we include current element
	inc = ar[0]
	
	#if we donot include current element
	exc = 0
	
	for i in range(1, n):
		inc1 = exc+ar[i]
		
		exc1 = max(inc, exc) #max sum before this point
		
		inc, exc = inc1, exc1 
		
	print(max(inc,exc))