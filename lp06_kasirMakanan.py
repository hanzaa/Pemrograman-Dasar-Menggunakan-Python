# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 15:18:20 2020

@author: M. Farhan Zachary
"""

h=float(input('Masukan harga makanan :'))
pajak=0.10*h
tip=0.18*h
total=h+pajak+tip
print('\nHarga makanan\t:{:.2f}'.format(h))
print('Pajak\t:{:.2f}'.format(pajak))
print('Tip\t:{:.2f}'.format(tip))
print('Total Harga\t:{:.2f}'.format(total))