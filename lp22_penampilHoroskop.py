print("=== Program Penampil Horoskop ===")

bulan=str(input("Kamu lahir bulan apa ? ")).lower()
tanggal=int(input("Tanggal berapa ? "))
if bulan=="januari":
    if tanggal <= 19:   
     horoskop="Carpicorn"
    else:
     horoskop="Aquarius"
if bulan=="februari":
    if tanggal <= 18: 
     horoskop="Aquarius"
    else:
     horoskop="Pisces"
if bulan=="maret":
    if tanggal <= 20: 
     horoskop="Pisces"
    else:
     horoskop="Aries"
if bulan=="april":
    if tanggal <= 19: 
     horoskop="Aries"
    else:
     horoskop="Taurus"
if bulan=="mei":
    if tanggal <= 20: 
     horoskop="Taurus"
    else:
     horoskop="Gemini"
if bulan=="juni":
    if tanggal <= 20: 
     horoskop="Gemini"
    else:
     horoskop="Cancer"
if bulan=="juli":
    if tanggal <= 22: 
     horoskop="Cancer"
    else:
     horoskop="Leo"
if bulan=="agustus":
    if tanggal <= 22: 
     horoskop="Leo"
    else:
     horoskop="Virgo"
if bulan=="september":
    if tanggal <= 22: 
     horoskop="Virgo"
    else:
     horoskop="Libra"
if bulan=="oktober":
    if tanggal <= 22: 
     horoskop="Libra"
    else:
     horoskop="Scorpio"
if bulan=="november":
    if tanggal <= 21: 
     horoskop="Scorpio"
    else:
     horoskop="Sagitarius"
if bulan=="desember":
    if tanggal <= 21: 
     horoskop="Sagitarius"
    else:
     horoskop="Carpicorn"

print("Horoskop kamu adalah",horoskop)