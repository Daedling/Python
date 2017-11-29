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
            c+=1
            if v.endswith('.') or v.endswith(','):
                b+=1

    if c == 0:
        c=1
    print(str(int((c-b)/c*100))+'%')
else:
    print("Фаил пуст")
