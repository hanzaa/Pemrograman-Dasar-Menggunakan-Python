import math
print('=== Program Mencari Jarak antara Dua Titik di Bumi Menggunakan Garis Lintang dan Bujur ===')
print('Titik 1:')
a=math.radians(float(input('Masukan garis lintang\t:')))
b=math.radians(float(input('Masukan garis bujur\t:')))

print('Titik 2:')
c=math.radians(float(input('Masukan garis lintang\t:')))
d=math.radians(float(input('Masukan garis bujur\t:')))

jarak=6371.01*math.acos(math.sin(a)*math.sin(c) + math.cos(a)*math.cos(c)*math.cos(b-d) )

print ('jarak antara 2 titik tersebut adalah',jarak,'kilometer')
