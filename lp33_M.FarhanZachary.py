print("=== Program Pengonversi Desimal ke Biner ===")
desimal=int(input("masukan bilangan desimal = "))
biner=" "
while desimal>0:
    if desimal%2==0:
        biner="0"+biner
    else:
        biner="1"+biner
    desimal=desimal//2
print("binarinya adalah = ",biner)
    
