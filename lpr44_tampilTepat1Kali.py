print("=== Menampilkan Tepat Satu Kali Inputan ===")

daftar=[]
barang=input('Masukan barang\t:')
daftar.append(barang)

barang=input('Masukan barang\t:')
while barang != '':
    n=0
    for i in range(len(daftar)):
        if barang==daftar[i]:
            n+=1
    if n==0:
        daftar.append(barang)
    barang=input('Masukan barang\t:')

print(" Daftar Barang ".center(30,'='))
for i in range(len(daftar)):
    print(daftar[i])

