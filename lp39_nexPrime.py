def bilPrima(bil):
    jwb=True
    for i in range (2,bil):
        if bil%i==0:
            jwb=False
            break
    return jwb

def nexPrime(n):
    n=n+1
    jwb=True
    while True:
        if bilPrima(n):
            jwb=False
            return n
        else:
            n+=1
def main():
    print("=== NexPrime ===")
    a=int(input('Masukan bilangan\t:'))
    b=nexPrime(a)
    print('Bilangan prima yang lebih besar dari',a,'adalah',b)

if __name__ == "__main__":
    main()
       
   
