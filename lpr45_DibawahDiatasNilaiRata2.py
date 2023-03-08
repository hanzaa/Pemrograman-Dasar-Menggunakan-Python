print('=== Program Pengolah Nilai ===')
daftar=[]
l=True
while l==True:
    a=(input("Masukan Nilai \t:"))
    if  a =='':
        l=False
    else:
        daftar.append(int(a))

#mencari rata-rata inputan
avg=sum(daftar)/len(daftar)
print('Rata-rata = ',avg)

#semua nilai dibawh rata-rata
daftar.append(avg)
daftar.sort()
print('Nilai dibawah rata-rata = ',daftar[:daftar.index(avg)])
daftar.reverse()
daftar.remove(avg)

#semua nilai rata-rata
rata2=[]
for i in daftar:
    if i == avg :
        rata2.append(i)        
print('Nilai rata-rata:',rata2)

#semua nilai diatas rata-rata
daftar.append(avg)
daftar.sort()
daftar.reverse()
print('Nilai diatas rata-rata:',daftar[:daftar.index(avg)])
daftar.remove(avg)



