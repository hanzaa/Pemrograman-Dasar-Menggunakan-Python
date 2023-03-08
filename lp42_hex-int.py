import math
print ("=== Program Pengnoversi Hex-Int dan sebaliknya ===")
def hexToDec(hexi):
    result = 0
    hexi = hexi.upper()
    for i in range(len(hexi)):
        cur_pow = len(hexi) - i  - 1
        if hexi[i] == 'A':
            result = result + (10 * math.pow(16,cur_pow))
        elif hexi[i] == 'B':
            result = result + (11 * math.pow(16,cur_pow))
        elif hexi[i] == 'C':
            result = result + (12 * math.pow(16,cur_pow))
        elif hexi[i] == 'D':
            result = result + (13 * math.pow(16,cur_pow))
        elif hexi[i] == 'E':
            result = result + (14 * math.pow(16,cur_pow))
        elif hexi[i] == 'F':
            result = result + (15 * math.pow(16,cur_pow))
        else:
            result = result + (int(hexi[i]) * math.pow(16,cur_pow))
    return int(result)
def dectoHex(dec):
    digits = "0123456789ABCDEF"
    dec = int(dec)
    x = (dec % 16)
    rest = dec // 16
    if (rest == 0):
        return digits[x]
    return dectoHex(rest) + digits[x]
s = str(input("Ingin melakukan convert?(y/n): "))
while s == 'y':
    print ("Pilihan :")
    print ("1. Hex to Dec")
    print ("2. Dec to Hex")
    n = int(input("Input Pilihan(1/2): "))
    if n == 1 :
        num = str(input("Input Hex: "))
        print ("Hex to Dec: ",hexToDec(num))
    else :
        num = str(input("Input Dec: "))
        print ("Dec to Hex: ",dectoHex(num)) 
    s = str(input("Ingin melakukan convert lagi?(y/n): "))