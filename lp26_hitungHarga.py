harga_asli=[500000,300000,150000,100000]
print ("Harga Asli\tJumlah diskon\tHarga baru")
for i in harga_asli:
    print ("{:.2f}\t{:.2f}\t{:.2f}".format(i,0.6*i,i-0.6*i))