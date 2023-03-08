print('=== Menambahkan Nomor ke Dalam File ===')
var=True
while var==True:
    try:
        namaFile=input('Masukan Nama File:')
        fp=open(namaFile,"r")
        data = fp.read()
        fileBaru=input('Masukan nama file baru yang ingin dibuat:')
        fb=open(fileBaru,'w+')
        var=False
    except UnicodeDecodeError:
        print('!! Format file tidak didukung !!')
    except FileNotFoundError:
        print('!! Data Tidak Ditemukan !!')

else:
    x = data.split('\n')
    a=''
    for i in range (len(x)):
        print (i+1," : ",x[i])
        c=str((i+1))+' : '+str(x[i])
        a+=c+'\n'
    fb.write(a)    
    fp.close()
    fb.close()
    print('File baru telah dibuat:',fileBaru)


