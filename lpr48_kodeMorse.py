print(' Program Pembuat Kode Morse '.center(35,'='))
spasi=' '
kodeMorse={'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.',
           'f':'..-.','g':'--.','h':'....','i':'..','j':'.---',
           'k':'-.-','l':'.-..','m':'--','n':'-.','o':'---',
           'p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-',
           'u':'..-','v':'...-','w':'.--','x':'-..-','y':'-.--',
           'z':'--..','0':'-----','1':'.----','2':'..---','3':'...--',
           '4':'....-','5':'.....','6':'-....','7':'--...','8':'---..',
           '9':'----.'
           }
pesan=str(input('Masukan pesan yang ingin diubah:\n')).lower()
print('kodenya adalah:',)

for huruf in pesan:
    if huruf.isalnum():
        print(kodeMorse[huruf],' ',end='')