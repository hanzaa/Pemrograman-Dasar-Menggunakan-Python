def cari():
    try:
        x=['']
        y=[]
        z=0
        a=input('Masukkan Nama file : ')
        A=open(a,"r")
        while True:
            isi=A.readline()
            x.append(isi)
            if not isi:
                x.pop()
                break
        for i in range(1,len(x)):
            if(x[i].count('def')>0):
                if(x[i-1].count('#')==0):
                    y.append(i)
        for j in range(0,len(y)):
            print('Jangan lupa memberi komentar pada fungsi, baris ke-',y[j])
            z +=1
        A.close()
    except FileNotFoundError:
        print('Maaf file tersebut tidak ada')
        z=1
    finally:
        if(z==0):
            print('Hmm, anda teliti ya')
        else:
            pass
def main():
    try:
        a=int(input('''Program pengingat komentar ! ("#")
Ingin berapa kali pengecekan? : '''))
        for i in range(0,a):
            cari()
    except:
        print('Maaf Data tidak valid')
if __name__=="__main__":
    main()