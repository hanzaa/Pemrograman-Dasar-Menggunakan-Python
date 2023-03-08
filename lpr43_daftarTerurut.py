print('=== Program Ini akan Mengurutkan Data yang Kamu Input ===')
print('Masukan nilai 0 untuk mulai mengurutkan')
daftar=[]
a=int(input('masukan nilai:'))
while a != 0:
    daftar.append(a)
    a=int(input('masukan nilai:'))

for i in sorted(daftar):
    print(i)