print('=== Proporsi Kata Dalam File ===')
var=True
while var==True:
    try:
        namaFile=input('Masukan Nama File:')
        with open(namaFile,'r') as f:
            baca=f.read().upper().split()
        var=False
    except UnicodeDecodeError:
        print('!! Format file tidak didukung !!')
    except FileNotFoundError:
        print('!! Data Tidak Ditemukan !!')

proporsi=[]
huruf=[]
for x in range (ord('A'),ord('Z')+1):
    hitung=0
    for y in range(len(baca)):
        if chr(x) in baca[y]:
            hitung+=1
    proporsi.append(hitung)
    huruf.append(chr(x))
    print('Proposi kata huruf',chr(x),':',hitung,'kata')

print('='*30)
print(' Proposi Kata Terkecil '.center(30,'-'))
for i in range(len(proporsi)):
    if min(proporsi)==0:
        if proporsi[i]==min(proporsi)+1:
            print('Huruf',huruf[i],':',proporsi[i],'kata')
    else:
        if proporsi[i]==min(proporsi):
            print('Huruf',huruf[i],':',proporsi[i],'kata')
