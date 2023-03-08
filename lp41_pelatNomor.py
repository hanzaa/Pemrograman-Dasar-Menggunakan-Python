import random
def pelat():
    jwb=''
    for i in range(2):
        a=random.randint(65,90)
        jwb+=chr(a)
    jwb+=" "
    for z in range(4):
        if z==0:
            b=random.randint(1,9) 
        else:   
            b=random.randint(0,9)
        jwb+=str(b)
    return jwb
def main():
    print('=== Generate Random Pelat Number ===')
    cek=str(input('Generate pelat(y/n):'))
    while cek == "y":
        print(pelat())
        cek=str(input('Generate pelat(y/n):'))
if __name__ == "__main__":
    main()   

