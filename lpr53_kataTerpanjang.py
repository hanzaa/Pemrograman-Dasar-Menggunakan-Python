print('=== Identifikasi Kata Terpanjang ====')
var=True
while var==True:
    try:
        namaFile=input('Masukan Nama File:')
        f=open(namaFile,"r")
        baca=f.read().split()
        var=False
    except UnicodeDecodeError:
        print('!! Format file tidak didukung !!')
    except FileNotFoundError:
        print('!! Data Tidak Ditemukan !!')
count=[]
for i in range(0,len(baca)):
    count.append(len(baca[i]))

print('===== Kata terpanjang =====')
for i in range (0,len(baca)):
    if(len(baca[i])==max(count)):
        print('-',baca[i],'(',len(baca[i]),'huruf)')