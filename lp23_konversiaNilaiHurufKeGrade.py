print ('=== Program Pengonversi Nilai dari Huruf ke Grade ===')
n={'A+':4.0,'A':4.0,'A-':3.7,'B+':3.3,'B':3.0,'B-':2.7,'C+':2.3,'C':2.0,'C-':1.7,'D+':1.3,'D':1.0,'F':0}

nil=input("Masukan nilai kamu\t:")
if nil in n :
   print("nilai",nil,"=",n[nil])
else:
   print("Nilai tidak valid")