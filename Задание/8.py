f=0
res=''
with open('freq.txt', encoding='utf-8') as k:
    z=k.readlines()
    for y in z:
        y=y.replace('\n','')
        w=y.split(' | ')
        if 'част' in w[1].split():
            res+=w[0]+', '
            f+=float(w[2])
print(res[:(len(res)-2)])
print(f)
