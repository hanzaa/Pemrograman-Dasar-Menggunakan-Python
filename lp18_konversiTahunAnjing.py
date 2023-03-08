print('=== Program Pengonversi Tahun Manusia ke Tahun Anjing ===')
usia=float(input('Masukan Tahun Manusia\t:'))
if 0 < usia <= 21:
    anjing=usia/10.5
    print("Usia anda setara dengan",anjing,"tahun anjing")
elif usia <0:
    print("Usia tidak nyata dalam realitas")
else:
    anjing=2+0.25*(usia-21)
    print("Usia anda setara dengan",anjing,"tahun anjing")


