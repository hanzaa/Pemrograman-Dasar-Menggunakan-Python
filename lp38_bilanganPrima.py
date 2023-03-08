def bilPrima(bil):
    jwb=True
    for i in range (2,bil):
        if bil%i==0:
            jwb=False
            break
    return jwb
   

def main():
    print('=== Program Pemeriksa Bilangan Prima ===')
    a=int(input('Masukan bilangan\t:'))
    b=bilPrima(a)
    if b == True:
        print('prima')
    elif b != True:
        print('bukan prima')
if __name__ == "__main__":
    main()
