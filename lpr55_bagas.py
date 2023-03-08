def main():
    try:
        trans=''
        print('Program pencari kata yang paling banyak dipakai')
        a=input('Masukkan file yang akan diidentifikasi : ')
        A=open(a,"r")
        narasi=A.read()
        print('\nMohon bersabar :)\n')
        for i in range(0,len(narasi)):
            if(chr(65)<=narasi[i]<=chr(90))or(chr(97)<=narasi[i]<=chr(122))\
                or(narasi[i]==' ')or(narasi[i]=='\t')or(narasi[i]=='\n'):
                trans=trans+narasi[i]
        trans1=trans.lower().split()
        x=[]
        y=[]
        for j in range(0,len(trans1)):
            x.append(trans1[j])
            y.append(trans1.count(trans1[j]))
            for k in range(0,len(x)+1):
                if(x.count(trans1[k])>1):
                    x.pop()
                    y.pop()
        print(x)
        print(y)
        print('Kata yang sering dipakai adalah :')     
        for l in range(0,len(x)):
            if(y[l]==max(y)):
                print('- "'+x[l]+'" sebanyak :',max(y),'kali')
        A.close()
    except FileNotFoundError:
        print('Maaf, file tersebut invalid')
if __name__=="__main__":
    main()