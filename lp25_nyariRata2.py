print("=== Program Pencari Nilai Rata-Rata ===")
print("\nSilahkan masukan nilai yang ingin dicari rata-ratanya")
print("Masukan nilai 0 untuk mulai mencari")

data=float(input("Masukan data\t:"))
jumlah=0 #Variabel penjumlahan seluruh data
n=0 #Banyaknya data yang diinput


if data == 0:
    print("Error:data pertama tidak boleh 0")
while data != 0:
    n=n+1
    jumlah=jumlah+data
    data=float(input("Masukan data \t:"))
    if data == 0:
        print("rata-rata=",jumlah/n)
    
           