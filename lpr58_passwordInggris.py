print ("=== Program Penghasil Sandi B.Inggris ===")

def main():
    import random
    with open ("daftarKataInggris.txt","r") as fp :
        data = fp.read().split()
    a=data[random.randrange(len(data))]  
    b=data[random.randrange(len(data))]
    if len(a)+len(b)==random.randint(8,10):
        print('Password\t:',a+b)
    else:
        main()

if __name__ == "__main__":
    main()
