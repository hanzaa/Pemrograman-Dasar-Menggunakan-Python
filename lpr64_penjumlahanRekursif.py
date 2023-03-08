def jumlah():
    angka=input("Masukan angka\t:")
    if angka=="":
        return 0
    else:
        return (float(angka)+jumlah())
print('=== Penjumlahan Angka ===')
hasil=jumlah() 
print('hasil\t:',hasil)
