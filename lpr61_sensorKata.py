def main():
    try:
        print('Program penyunting file')
        A=input('Masukkan nama file yang akan disunting: ')
        a=open(A,"r")
        B=input('Masukkan nama file terdapat kata-kata sensitif: ')
        b=open(B,"r")
        C=input('Masukkan nama file setelah disunting: ')
        c=open(C,"w+")
        narasi=a.read()
        trans1=narasi.lower()
        x=b.read().split()
        for i in range(0,len(x)):
            M=''
            for j in range(0,len(x[i])):
                M=M+'*'
            trans1=trans1.replace(x[i],M)
            M=''
        trans2=''
        for k in range(0,len(narasi)):
            if(trans1[k]=='*'):
                trans2=trans2+'*'
            else:
                trans2=trans2+narasi[k]
        c.write(trans2)
        a.close()
        b.close()
        c.close()
    except FileNotFoundError:
        print('Maaf, file invalid')
if __name__=="__main__":
    main()