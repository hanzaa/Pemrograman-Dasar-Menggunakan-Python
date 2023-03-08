
def tarif(jarak):
    ongkos = 10000 + jarak*8000
    return ongkos
def main():
    print('=== Program Penghitung Tarif Taksi ===')
    a=float(input('Berapa jauh jarak perjalanannya(KM)? '))
    b=tarif(a)
    print('Ongkos = Rp',b)

if __name__ == "__main__": 
    main()
