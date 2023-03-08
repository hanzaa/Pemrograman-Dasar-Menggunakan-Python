# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 14:27:07 2020

@author: M. Farhan Zachary
"""
print('Selamat datang\nSilahkan masukan jumlah botol yang anda punya')
a=int(input('Botol <= 1 liter:\t'))
b=int(input('Botol > 1 liter:\t'))

harga1=a*0.10
harga2=b*0.25
harga3=harga1+harga2

print('\nJumlah botol =',a+b)
print('Deposit yang akan diterima= $ {:.2f}'.format(harga3))