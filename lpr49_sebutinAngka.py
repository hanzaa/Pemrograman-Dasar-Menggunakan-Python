def Terbilang(bil):
    angka=["nol","Satu","Dua","Tiga","Empat","Lima",
    "Enam","Tujuh","Delapan",
    "Sembilan","Sepuluh","Sebelas"]
    Hasil =" "
    n = int(bil)
    if n >= 0 and n <= 11:
        Hasil = Hasil + angka[n]
    elif n < 20:
        Hasil = Terbilang(n % 10) + " Belas"
    elif n < 100:
        Hasil = Terbilang(n / 10) + " Puluh" + Terbilang(n % 10)
    elif n < 200:
        Hasil = " Seratus" + Terbilang(n - 100)
    elif n < 1000:
        Hasil = Terbilang(n / 100) + " Ratus" + Terbilang(n % 100)
    else:
        Hasil="Angka hanya sampai 999"
    return Hasil

def main() :
    print("=== Program Konversi Angka Menjadi Kata ===")
    a=int(input('Masukan angkanya:\n'))
    print('Anda memasukan:',Terbilang(a),'rupiah')


if __name__ == "__main__":
    main()