print("=== Program Pengecek Kalimat Parlindrom ===")
text = input("Masukan kalimat\t:")
rev=""
for i in range (len(text)-1,-1,-1):#ingat index dimulai dari 0
    rev+=text[i]
if text == rev:
    print("kalimat",text,"merupakan parlindom")
else:
    print("kalimat",text,"bukan merupakan parlindom")