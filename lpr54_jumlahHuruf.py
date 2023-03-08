print('=== Menentukan Jumlah Huruf dalam File === ')
var=True
while var==True:
    try:
        namaFile=input('Masukan Nama File:')
        fp=open(namaFile,"r")
        baca=fp.read().upper().split()
        var=False
    except UnicodeDecodeError:
        print('!! Format file tidak didukung !!')
    except FileNotFoundError:
        print('!! Data Tidak Ditemukan !!')
else:
    jwb=[]
    x=[]
    for kata in baca:
        for huruf in kata:
            if huruf.isalpha() :
                x.append(huruf)
                if huruf not in jwb:
                    jwb.append(huruf)
    jwb.sort()
    for i in range (len(jwb)):
        print ('Huruf',jwb[i],'=',x.count(jwb[i]),'kata')