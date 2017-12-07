f=0
with open('freq.txt', encoding='utf-8') as k:
    z=k.readlines()
    for y in z:
        y=y.replace('\n','')
        w=y.split(' | ')
        if 'част' in w[1].split():
            print(y)
            f+=float(w[2])      
print(f)
