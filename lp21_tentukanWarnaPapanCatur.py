print('=== Program penentu warna kotak dalam papan catur ===')
print('Koordinat ditentukan dalam (huruf,angka)')
a=str(input('Masukan huruf\t:'))
b=int(input('Masukan angka\t:'))
c=ord(a)

if b%2==c%2:
    print('(',a,',',b,') merupakan kotak hitam')
else:
    print('(',a,',',b,') merupakan kotak putih')