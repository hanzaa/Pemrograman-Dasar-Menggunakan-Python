import random
def createDeck():
    kartu=[]
    for i in 'shdc' :
        for k in range(2,10):
            kartu.append('{}{}'.format(k,i))
        for n in 'TJQKA' :
            kartu.append('{}{}'.format(n,i))
    return kartu

def shuffle(kartu):
    acak=[]
    for i in range (52):
        acak.append(kartu.pop(random.randrange(0,len(kartu))))
    return acak


kartu=createDeck()
print('======= Deck Tersusun =======')
for i in range (13):
    print(kartu[i],'\t',kartu[i+13],'\t',
          kartu[i+26],'\t',kartu[i+39])

acak=shuffle(kartu)
print('======= Deck Teracak =======')
for i in range (13):
    print(acak[i],'\t',acak[i+13],'\t',
          acak[i+26],'\t',acak[i+39])
