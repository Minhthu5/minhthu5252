# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 20:41:49 2024

@author: PhamNguyenThiMinhThu
"""

a = "i'm a cat"
print(a[0].upper() + a[1:3] + a[3:].title())
print(a.upper())
print(a[:1].lower() + a[1:3].upper() + a[3:7].lower() + a[7:].upper())
print(a.capitalize())