import random
def sandi():
    jwb=''
    a=random.randint(7,10)
    for i in range(0,a):
        b=random.randint(33,126)
        jwb=jwb+chr(b)
    return jwb
def main():
    print('=== Penghasil Sandi Acak ===')
    cek=str(input('Generate sandi(y/n):'))
    while cek == "y":
        print(sandi())
        cek=str(input('Generate sandi(y/n):'))
        

if __name__ == "__main__":
    main()
    

