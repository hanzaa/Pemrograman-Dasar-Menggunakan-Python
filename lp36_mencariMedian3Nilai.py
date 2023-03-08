
def median(a,b,c):
    data=[a,b,c]
    for panjang in range(len(data)-1,0,-1):#loop bubble sort
        for i in range (panjang):
            if data[i]>data[i+1]:
                ganti=data[i]#variabel penampung
                data[i]=data[i+1]#data bertukar,switch!
                data[i+1]=ganti
    median=data[2]
    return median

def main():
    print('=== Program Pencari Nilai Median 3 Nilai === ')
    a=int(input('Masukan Nilai ke -1:'))
    b=int(input('Masukan Nilai ke -2:'))
    c=int(input('Masukan Nilai ke -3:'))
    print('mediannya adalah',median(a,b,c))

if __name__ == "__main__":
    main()


 
