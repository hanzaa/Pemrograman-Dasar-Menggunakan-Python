# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 16:21:41 2020

@author: M. Farhan Zachary
"""

"""
Efisiensi BBM Amerika = miles per gallon (MPG)
Efisiensi BBM Kanada = liter per 100 km (L/100 km)
1 MPG = 235.215 LP100KM
"""
a=float(input("Masukan efisiensi BBM dalam unit Miles per Gallon(mpg):"))
lp100km = 235.215/a
print(a,'mpg = ',lp100km,'liter/100 km')