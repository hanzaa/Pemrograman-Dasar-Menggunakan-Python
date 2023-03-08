print("=== Program Pencari Nilai Kembalian Pembayaran ===")
print()
a=float(input("Masukan Jumlah Uang Pelanggan:\t"))
b=float(input("Masukan Harga Yang Harus di Bayar:\t"))
diskon=b%1000%500%100%50%25
print('Diskon =',diskon,'Rupiah')
print("Total =",b-diskon,'Rupiah')
c=a-(b-diskon)
print("Kembalian=",c)
print()
sisa1=c//1000 
sisa2=c%1000//500
sisa3=c%1000%500//100
sisa4=c%1000%500%100//50
sisa5=c%1000%500%100%50//25
"""
sintaks // berfungsi menampilkan hasil pembagian tanpa koma.
contoh:15//2 = 7
sintaks % berfungsi menampilkan sisa hasil pembagian
contoh 15%2 = 1
"""
print('koin 1000:',sisa1,'buah')
print('koin 500:',sisa2,'buah')
print('koin 100:',sisa3,'buah')
print('koin 50:',sisa4,'buah')
print('koin 25:',sisa5,'buah')

