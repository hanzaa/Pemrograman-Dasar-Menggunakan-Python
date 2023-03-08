print('=== Program Tabel Unsur Periodik ===')
proton=[]
simbol=[]
nama=[]
with open('tabel periodik.txt','r') as ft:
    for unsur in ft.readlines():
        x=unsur.split()
        proton.append(x[0])
        simbol.append(x[1].lower())
        nama.append(x[2].lower())

try:
    x=input('Masukan lambang atom/jumlah proton atom\t:').lower()

    if x.isalpha():
        for i in range(len(nama)):
            if x==nama[i]:
                print('jumlah proton',x,'=',proton[i])

        for i in range(len(simbol)):
            if x==simbol[i]:
                print('jumlah proton',x,'=',proton[i])

    elif x.isdigit():
        x=int(x)
        print('(',simbol[x-1],')',nama[x-1],':jumlah proton =',proton[x-1])
except:
        print ("Nilai yang anda masukkan tidak sesuai dengan unsur manapun.")




