import random
def ran(list):
    return(random.choice(list))
def constr():
    r=0
    while r ==0:
        r=0
        z=[V(op()),I_VII(op()),V(op()),I_VII(op()),I_VII(op())]
        for ct, a in enumerate(z):
            if a[len(a)-1]!=',' and a[len(a)-1]!='.'and ct!=4:
                z[ct]+=','
            if ct==4 and z[ct][len(a)-1]!='.':
                z[ct]+='.'  
            if a[len(a)-1]=='.':
                r+=1
        for a in z:
            print(a.capitalize())
def op():
    with open('lists.txt', 'r', encoding='utf-8') as k:
        c=k.readlines()
        for ct, a in enumerate(c):
            c[ct]=a.strip('\n')
        for ct, a in enumerate(c):# без этого оставляет при последнем элементе cтроки \n
            c[ct]=a.split('\t')
        return(c)   
def V(list):
    s=ran(list[10])+' '+ran(list[9])+'.'
    w=ran(list[8])+' '+ran(list[7])
    v=ran(['на '+ran(list[6])+' '+ran(list[3]),'на '+ran(list[3])+' '+ran(list[6])])
    j=ran(['на '+ran(list[5])+' '+ran(list[4]),'на '+ran(list[4])+' '+ran(list[5])])
    x=ran(['в '+ran(list[4])+' '+ran(list[1]),'в '+ran(list[1])+' '+ran(list[4])])
    y=ran(['в '+ran(list[3])+' '+ran(list[2]),'в '+ran(list[2])+' '+ran(list[3])])
    z=[x,y,v,w,s]
    return(ran(z))
def I_VII(list):
    v=ran(list[15])+', '+ran(list[16])+', '+ran(list[17])+'.'
    j='не '+ ran(list[18])+' '+ran(list[19])
    y='но c '+ran(list[11])
    x=ran([ran(list[12])+' '+ran(list[13])+' '+ran(list[14]),ran(list[13])+' '+ran(list[14])+' '+ran(list[12])])+'.'
    z=ran(list[20])+' '+ran(list[22])+' '+ran(list[21])+'.'
    return(ran([x,y,z,j,v]))
def main():
    constr()
    x=input('Ещё? (Y)\n')
    while x=='Y':
        print('\n')
        constr()
        x=input('Ещё? (Y)\n')
if __name__ == '__main__':
    main()                          
                                  
   

