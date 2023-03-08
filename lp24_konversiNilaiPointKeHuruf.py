print ('Program Mengetahui Grade Huruf dari Grade Point')
print ('----------------------------------------------')
n = float(input('Masukkan Nilai Anda: '))
if n==4.00:
    print('Grade Huruf Anda adalah A+')
elif 3.71<=n<=3.99:
    print('Grade Huruf Anda adalah A')
elif 3.31<=n<=3.70:
    print('Grade Huruf Anda adalah A-')
elif 3.01<=n<=3.30:
    print('Grade Huruf Anda adalah B+')
elif 2.71<=n<=3.00:
    print('Grade Huruf Anda adalah B')
elif 2.31<=n<=2.70:
    print('Grade Huruf Anda adalah B-')
elif 2.01<=n<=2.30:
    print('Grade Huruf Anda adalah C+')
elif 1.71<=n<=2.00:
    print('Grade Huruf Anda adalah C')
elif 1.31<=n<=1.70:
    print('Grade Huruf Anda adalah C-')
elif 1.01<=n<=1.30:
    print('Grade Huruf Anda adalah D+')
elif 0.01<=n<=1.00:
    print('Grade Huruf Anda adalah D')
elif n == 0:
    print('Grade Huruf Anda adalah D-')
else:
    print ('Error')