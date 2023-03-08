# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 15:49:33 2020

@author: M. Farhan Zachary
"""

t0=float(input('Berapa Nilai Tabungan Anda ? '))
t1=t0*(1.04)**1
t2=t0*(1.04)**2
t3=t0*(1.04)**3
print('Saldo tabungan tahun pertama ={:.2f}'.format(t1))
print('Saldo tabungan tahun kedua ={:.2f}'.format(t2))
print('Saldo tabungan tahun ketiga ={:.2f}'.format(t3))


