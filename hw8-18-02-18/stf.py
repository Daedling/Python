import random
def extract():
    with open ('csv.csv', 'r', encoding='utf-8') as k:
        d=[]
        k=list(k)
        for a in k:
            d.append(a.strip('\n'))
        return d
def corrnga(d):     
    rng=d[0].split(',')
    del d[0]    
    crr=d[0].split(',')
    del d[0]
    dct={}
    words=[]
    for a in d:
        a=a.split(',')
        words.append(a[0])
        dct[a[0]]=a[1:len(a)]
    word=random.choice(words)
    hlp=random.choice(dct[word])
    return(word,hlp,rng,crr)
def out(b):
    fin = 1
    while fin !=0:
        resp=''
        print ("Введите пропущенное слово с большой буквы. \n"+b[1])
        resp=input("Ответ: ")
        if resp !=b[0]:
            print(random.choice(b[2]))
        else:
            print(random.choice(b[3]))
        ind=input("Еще раз? (Y/N)")
        if ind == 'Y':
            out(corrnga(extract()) )
            break
        elif ind == 'N':
            fin = 0
        else:
            print("Такого не знаю.")
            break
if __name__ == '__main__':
    out(corrnga(extract()))
    print('Конец.')
    
