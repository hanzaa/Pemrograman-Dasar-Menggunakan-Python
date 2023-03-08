def cat(a):
    # try:   
        output=''
        for i in range (len(a)):
            file=open('{}.txt'.format(a[i]))
            isi=file.readlines()
            for i in isi:
                output+=i
        print('Isi File :')
        print(output)

    # except FileNotFoundError:
    #     print('!! File tidak ditemukan !!')

def main():
    print('=== Menampilkan 2/lebih file ===')
    daftarFile=[]
    file=input('Masukan nama file:')
    daftarFile.append(file)
    tanya=input('Mau menambah file (y/n) ? ')
    while tanya == 'y':
        file=input('Masukan nama file:')
        daftarFile.append(file)
        tanya=input('Mau menambah file (y/n) ?')
     
    print('='*30)
    cat(daftarFile)  
    
    

if __name__ == "__main__":
    main()
