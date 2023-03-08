print("=== Program Penentu Tingkat Kebisingan ===")
kebisingan={130:'Jackhammer',106:'Pemotong rumput',70:'Jam weker',40:'Ruangan hening' }

db=int(input())

if db in kebisingan:
    print('Kebisingan setara dengan',kebisingan[db])
elif db > 130:
    print('Kebisingan lebih dari Jackhammer')
elif 106 < db < 130:
    print('Kebisingan diantara Jackhammer dan Pemotong rumput')
elif 70 < db < 106:
    print('Kebisingan diantara Pemotong rumput dan Jam weker')
elif 40 < db < 70:
    print('Kebisingan diantara Jam weker dan Ruangan hening')
elif db < 40:
    print('Kebisingan kurang dari ruangan hening')

