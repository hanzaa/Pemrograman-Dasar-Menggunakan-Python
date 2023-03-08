print('=== Program Enkripsi Pesan:Caesar Chiper ===')
#Variabel
pesan_asli=input('Masukan pesan yang ingin di enkripsi\t:').lower()# unicode untuk a dan A berbeda jadi diseragamkan pakai lower()
pergeseran=int(input('Berapa banyak pergeserannya? '))
hasil_enkripsi=''

#loop
for huruf in pesan_asli:
    if huruf.isalpha()==True: #isalpha()mendeteksi inputan berupa huruf(a,b,c)bukan yg lain(!,@?)
        x=ord(huruf)-97
        x += pergeseran
        x= x % 26
        hasil_enkripsi += chr(x+97)
    else:
        hasil_enkripsi += huruf
#hasil
print(hasil_enkripsi)

        
        