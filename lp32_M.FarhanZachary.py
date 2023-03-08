print("=== Program Pengonversi Biner ke Desimal ===")
biner=input("masukan bilangan biner = ")
desimal=0
for i in range (len(biner)):
    angka=biner[(len(biner)-1)-i]
    angka=int(angka)
    if angka==1:
        desimal=desimal+pow(2,i)

print("bilangan desimalnya adalah = ",desimal)
