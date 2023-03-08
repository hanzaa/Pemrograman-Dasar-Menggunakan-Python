print('=== Menemukan Kata Paling Sering Muncul dalam File ===')

var=True
while var==True:
    try:
        namaFile=input('Masukan Nama File:')
        fp=open(namaFile,"r")
        baca=fp.read().lower().split()
        var=False
    except UnicodeDecodeError:
        print('!! Format file tidak didukung !!')
    except FileNotFoundError:
        print('!! Data Tidak Ditemukan !!')
kataDalamFile=[]
hitung=[]
    
for i in range(len(baca)):
    if baca[i] not in kataDalamFile:
        kataDalamFile.append(baca[i])
        hitung.append(baca.count(baca[i]))

print('===== Kata Paling Sering Muncul =====')
for i in range (len(kataDalamFile)):
    if hitung[i]==max(hitung):
        print(kataDalamFile[i],'muncul',hitung[i],'kali')
