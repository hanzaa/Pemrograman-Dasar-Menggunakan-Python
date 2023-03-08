print('=== Program Pengonversi Nilai A/B/C/D/E ke Angka dan Sebaliknya ===')
grade={'A':85,'B':70,'C':55,'D':40,'E':0}

var=True
while var==True:
    try:
        a=input('Masukan nilai :').upper()
        if a=='':
            print('++ selesai ++')
            var=False
        elif chr(65) <= a <= chr(69):
            print(a,'=',grade[a])
        else:
            a=float(a)
            for key,value in grade.items():
                if a>=value:
                    print(a,'=',key)
                    break
    except:
        print('--salah--')
    
