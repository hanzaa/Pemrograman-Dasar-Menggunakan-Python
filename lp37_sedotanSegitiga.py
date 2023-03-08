def segitiga(a,b,c):
    if a >= b+c:
        return False

    elif b >= a+c:
        return False

    elif c >= a+b:
        return False
    else:
        return True
def main():
    print('Apakah sedotan mu dapat membentuk segitiga? ')
    a=float(input('Masukan panjang sedotan ke-1:'))    
    b=float(input('Masukan panjang sedotan ke-2:'))         
    c=float(input('Masukan panjang sedotan ke-3:')) 
    print(segitiga(a,b,c))        
if __name__ == "__main__":
    main()