print('=== Menjumlahkan Angka ===')
var=True
b=float()
while var==True:
    try:
        a=input('Masukan angka\t:')
        
        while a!='':
            b=b+float(a)
            print('Hasil Sementara\t:',b)
            print('='*25)
            a=input('Masukan angka\t:')
        print(' Hasil Akhir '.center(25,'='),'\n',b)
        var=False
    except :
        print('--error--')
        print("="*25)