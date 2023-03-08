import math as m

def hipotenusaSegitiga (sisi1,sisi2):
    return m.sqrt(sisi1**2+sisi2**2)

def main():
    print('=== Program Pencari Hipotenusa segitiga ===')
    a=float(input('Masukan panjang sisi 1\t:'))
    b=float(input('Masukan panjang sisi 2\t:'))
    c=hipotenusaSegitiga(a,b)
    print('Hipotenusa segitiga teresebut adalah',c)

if __name__ == "__main__":
    main()