def atur(n):
    if len(n)==1:
        return print(n[0])
    if len(n)==2:
        return print(n[0],' dan ',n[1])
    if len(n)>2:
        print(n[0],end="")    
        for i in range(1,len(n)-1):
            print(',',n[i],end='')
        print(' dan',n[-1])


def main():
    print('=== Daftar Barang ===')
    daftar=[]
    barang=input('Masukan barang\t:')
    while barang != '':
        n=0
        for i in range(len(daftar)):
            if barang==daftar[i]:
                n+=1
        if n==0:
            daftar.append(barang)
        barang=input('Masukan barang\t:')
    print('Anda memasukan:')
    atur(daftar)

   

if __name__ == "__main__":
    main()