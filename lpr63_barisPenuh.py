def main():
    M=[]
    a=open("Petualangan Alice di Negeri Ajaib.txt","r")
    b=a.read().split()
    x=0
    for i in range(0,len(b)):
        x=x+len(b[i])+2
        if(x<52):
            M.append(b[i]+' ')
            x -=1
        else:
            M.append('\n'+b[i]+' ')
            x=len(b[i])+1        
    for j in range(0,len(M)):
        print(M[j],end='')
if __name__ == "__main__":
    main()