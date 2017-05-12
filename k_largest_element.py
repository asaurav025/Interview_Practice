#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 11:47:47 2017

@author: ska
"""
import heapq

for _ in range(int(input())):
    n,k = map(int, input().split())
    li1 = list(map(int, input().split()))
    heapq.heapify(li1)
    li=heapq.nlargest(k, li1)
    li = map(str, li)
    print(" ".join(li))


