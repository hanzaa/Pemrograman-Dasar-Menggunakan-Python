print("=== Harga Tiket Masuk ===")
print("Silahkan masukan usia tiap orang")

usia=[]
total=0
while True:
    x=input('usia\t:')
    if x=='':
        break
    else:
        usia.append(int(x))
            
for i in range (len(usia)):
    if usia[i] < 3:
        total=total+0
    elif 3<=usia[i]<=12:
        total=total+50000
    elif usia[i]>=65:
        total=total+75000
    else:
        total=total+100000
        
print('Total harga tiket\t= Rp{:.2f}'.format(total))