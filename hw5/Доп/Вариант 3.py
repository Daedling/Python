r=[]
a=0
b=0
c=0
print('Имя фаила должно иметь вид "text.exe", пустые фаилы не принимаются')
with open('text.txt', encoding ='utf-8') as txt:
    k = txt.readlines()
if len (k) == 0:
    print ("пшол")
    a=1
if a!=1:
    for i in k:
        z=i.split()
        for v in z:
            if len(v)==1:
                b+=1
            if len(v)==3:
                c+=1
    if c == 0:
        print('Слов длины 3 нет')
    if b == 0:
        print('Слов длин 1 нет')
    else:   
        print(str(c/b))
else:
    print("Фаил пуст")
